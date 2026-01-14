#!/usr/bin/env python3
"""
Linear Status Sync Script
Fetches ticket statuses from Linear and updates the PRD markdown file.

This script is designed to be run by Claude Code in a GitHub Action
to keep the PRD ticket table up-to-date automatically.
"""

import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

# Configuration
LINEAR_API_URL = "https://api.linear.app/graphql"
PRD_PATH = "docs/prd.md"

def get_linear_api_key():
    """Get Linear API key from environment"""
    api_key = os.environ.get('LINEAR_API_KEY')
    if not api_key:
        raise ValueError("LINEAR_API_KEY not found in environment")
    return api_key

def fetch_project_tickets(project_name: str) -> list:
    """
    Fetch all tickets from a Linear project using GraphQL API.

    Args:
        project_name: Name of the Linear project (e.g., "TaskFlow Calendar Integration")

    Returns:
        List of ticket dictionaries with id, identifier, title, state, url
    """
    api_key = get_linear_api_key()

    query = """
    query GetProjectIssues($projectName: String!) {
        projects(filter: { name: { eq: $projectName } }) {
            nodes {
                id
                name
                issues {
                    nodes {
                        id
                        identifier
                        title
                        state {
                            name
                            type
                        }
                        url
                    }
                }
            }
        }
    }
    """

    payload = json.dumps({
        "query": query,
        "variables": {"projectName": project_name}
    }).encode('utf-8')

    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }

    req = urllib.request.Request(LINEAR_API_URL, data=payload, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        raise

    projects = data.get("data", {}).get("projects", {}).get("nodes", [])
    if not projects:
        print(f"Project '{project_name}' not found")
        return []

    issues = projects[0].get("issues", {}).get("nodes", [])

    tickets = []
    for issue in issues:
        tickets.append({
            "identifier": issue["identifier"],
            "title": issue["title"],
            "status": issue["state"]["name"],
            "url": issue["url"]
        })

    return tickets

def generate_ticket_table(tickets: list) -> str:
    """Generate markdown table from tickets"""
    if not tickets:
        return "| Ticket | Title | Status | Link |\n|--------|-------|--------|------|\n| _No tickets found_ | | | |"

    lines = [
        "| Ticket | Title | Status | Link |",
        "|--------|-------|--------|------|"
    ]

    for ticket in tickets:
        lines.append(
            f"| {ticket['identifier']} | {ticket['title']} | {ticket['status']} | [View]({ticket['url']}) |"
        )

    return "\n".join(lines)

def update_prd(tickets: list, prd_path: str = PRD_PATH) -> bool:
    """
    Update the PRD markdown file with current ticket statuses.

    Args:
        tickets: List of ticket dictionaries
        prd_path: Path to the PRD markdown file

    Returns:
        True if updated successfully, False otherwise
    """
    if not os.path.exists(prd_path):
        print(f"PRD file not found: {prd_path}")
        return False

    with open(prd_path, 'r') as f:
        content = f.read()

    # Generate new table
    new_table = generate_ticket_table(tickets)

    # Replace the ticket status section
    # Look for the table after "## Ticket Status"
    pattern = r'(## Ticket Status\n\n)(\|.*\n)+(\n---|\n_This PRD)'
    replacement = f'\\1{new_table}\n\n---'

    # Try to replace existing table
    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        # If no table found, try simpler pattern
        pattern = r'(\| Ticket \| Title \| Status \| Link \|\n\|[-|]+\|\n)(\|.*\n)*'
        new_content = re.sub(pattern, new_table + "\n", content)

    # Update timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_content = re.sub(
        r'Last updated.*\.',
        f'Last updated by Claude on {timestamp}.',
        new_content
    )

    with open(prd_path, 'w') as f:
        f.write(new_content)

    print(f"Updated {prd_path} with {len(tickets)} tickets")
    return True

def main():
    """Main entry point"""
    project_name = os.environ.get('LINEAR_PROJECT_NAME', 'TaskFlow Calendar Integration')

    print(f"Fetching tickets from Linear project: {project_name}")
    tickets = fetch_project_tickets(project_name)

    print(f"Found {len(tickets)} tickets:")
    for t in tickets:
        print(f"  - {t['identifier']}: {t['title']} [{t['status']}]")

    print(f"\nUpdating PRD...")
    success = update_prd(tickets)

    if success:
        print("Done!")
    else:
        print("Failed to update PRD")
        exit(1)

if __name__ == "__main__":
    main()
