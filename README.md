# Wox.Plugin.gh — GitHub Jump

A single-file Wox SDK plugin (Python) that jumps straight to a GitHub page:
a repository, one of its subpages, your fork of it, or your personal
pull-request and issue inboxes.

## Usage

Trigger keyword: `gh`

| Query | Result |
| --- | --- |
| `gh` | Shortcuts, plus your most recently pushed repositories |
| `gh pyst` | Fuzzy match against cached repository names |
| `gh danudey/pystrptime` | Open that repository |
| `gh danudey/pystrptime ` | List every page of that repository |
| `gh danudey/pystrptime releases` | Open that repository's releases page |
| `gh danudey/pystrptime rel` | Same — subpages are fuzzy matched too |
| `gh danudey/pystrptime fork` | Open your fork of that repository |
| `gh pulls` | Pull requests that involve you |
| `gh issues` | Issues that involve you |
| `gh notifications` | Your notification inbox |
| `gh refresh` | Rebuild the repository cache now |

An `owner/repo` you type in full always works, cached or not, so
`gh torvalds/linux releases` jumps there without the repository ever having been
fetched.

### Subpages

`code`, `issues`, `pulls`, `releases`, `actions`, `commits`, `branches`, `tags`,
`discussions`, `wiki`, `insights`, `security`, `forks`, `stargazers`,
`settings`, and `fork` (your own fork of the repository). Common aliases work:
`ci` and `workflows` reach Actions, `prs` reaches Pull requests, `docs` reaches
the Wiki.

If nothing matches, the filter text becomes a code search inside that
repository.

### Global shortcuts

`pulls`, `issues`, `notifications`, `gists`, `stars`, `profile`, `new`,
`explore`, `refresh`.

### Actions

Every repository row carries:

- **Open in browser** (Enter)
- **Browse pages** (Ctrl+B) — rewrites the query to `gh owner/repo ` so you can
  pick a subpage
- **Open issues** / **Open pull requests**
- **Copy URL**
- **Copy SSH clone command**

## Authentication

The plugin shells out to `gh auth token` and never stores a token of its own.
Run `gh auth login` once and everything works.

Navigation to an explicitly typed `owner/repo` and to the global shortcuts works
without authentication. Only repository autocomplete and fork resolution need a
token.

## Repository cache

The repository list comes from `GET /user/repos` with
`affiliation=owner,organization_member`, so it contains repositories you own and
repositories in organizations you belong to — nothing else. It is written to the
Wox plugin cache folder (`~/.wox/cache/plugins/<plugin-id>/repos.json`) and
refreshed in the background once it is older than the configured TTL.

## Settings

| Setting | Default | Meaning |
| --- | --- | --- |
| `gh` executable | `gh` | Path to the GitHub CLI. Platform specific, so it is not shared by cloud sync. |
| Refresh after | `24` h | How stale the cached repository list may get. |
| Include archived repositories | off | Show archived repositories in autocomplete. |
| Register repository names for inline Tab completion | off | Also registers up to 500 repository names as query commands. This turns on Wox's inline Tab completion for repository names, but adds one entry per repository to global search. Wox's own **Enable query completion hint** setting must be on for the inline hint to appear. |

## Install

Copy the single file into the Wox single-file plugin folder:

```sh
cp Wox.Plugin.gh.py ~/.wox/wox-user/plugins/single-file/
```

Wox watches that folder and reloads the plugin on save. Requires Wox 2.4.2 or
later and Python 3.10 or later.

## Implementation notes

- Standard library plus the Wox Python SDK only; no pip dependencies.
- Blocking work (`gh auth token`, HTTP, disk, launching the browser) runs through
  `asyncio.to_thread` so the shared Python runtime host is never stalled.
- Fork resolution happens off the query path: the first query shows
  "Looking for your fork…", the background lookup memoises the answer for ten
  minutes and calls `refresh_query`.
