# Atlassian OAuth App Setup Guide

This guide walks you through creating an OAuth 2.0 app in the Atlassian Developer Console.

## Step 1: Create Developer Account

1. Go to https://developer.atlassian.com/
2. Sign in with your Atlassian account
3. Click "Console" in the top navigation

## Step 2: Create New App

1. In the Developer Console, click "Create" > "OAuth 2.0 integration"
2. Enter a name for your app (e.g., "Claude Atlassian Skill")
3. Accept the developer terms
4. Click "Create"

## Step 3: Configure Permissions

### For Jira Access

1. Go to "Permissions" in the left sidebar
2. Click "Add" next to "Jira API"
3. Select these scopes:
   - `read:jira-work` - Read Jira project and issue data
   - `read:jira-user` - Read user information

### For Confluence Access

1. Click "Add" next to "Confluence API"
2. Select these scopes:
   - `read:confluence-content.all` - Read all Confluence content
   - `search:confluence` - Search Confluence
   - `readonly:content.attachment:confluence` - View attachments

## Step 4: Configure Authorization

1. Go to "Authorization" in the left sidebar
2. Click "Add" next to "OAuth 2.0 (3LO)"
3. Set the callback URL:
   ```
   http://localhost:9876/callback
   ```
4. Click "Save changes"

## Step 5: Get Credentials

1. Go to "Settings" in the left sidebar
2. Copy the **Client ID**
3. Copy the **Client Secret** (you may need to generate one)

## Step 6: Store Credentials

Run the setup command with your credentials:

```bash
uv run --directory /path/to/skill scripts/auth.py setup --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET
```

Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with values from step 5.

## Step 7: Authenticate

Run the login command to complete OAuth flow:

```bash
uv run --directory /path/to/skill scripts/auth.py login
```

This will:
1. Open your browser to Atlassian consent page
2. Ask you to grant permissions
3. Redirect back to capture the authorization
4. Store tokens securely in macOS Keychain

## Required Scopes Summary

| Scope | Purpose |
|-------|---------|
| `read:jira-work` | Read issues, comments, attachments |
| `read:jira-user` | Read user info for assignee/reporter |
| `read:confluence-content.all` | Read page content |
| `search:confluence` | CQL search |
| `readonly:content.attachment:confluence` | View attachments |
| `offline_access` | Refresh tokens (added automatically) |

## Troubleshooting

### "Invalid redirect URI"
Ensure the callback URL is exactly: `http://localhost:9876/callback`

### "Scope not authorized"
Go back to Permissions and ensure all required scopes are added.

### "Access denied"
Your Atlassian account needs access to the Jira/Confluence sites you're trying to access.

### Multiple Atlassian Sites
If you have access to multiple sites, the login process will ask you to choose one.

## Security Notes

- Client ID and Secret are stored in macOS Keychain
- Access tokens expire after 1 hour and auto-refresh
- Refresh tokens rotate (old ones become invalid)
- All credentials stay local on your machine
