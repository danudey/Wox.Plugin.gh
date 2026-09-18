# {
#   "Id": "9c6ddcda-0edf-4574-af3e-96bab47ef845",
#   "Name": "GitHub Jump",
#   "Author": "danudey",
#   "Website": "https://github.com/danudey/Wox.Plugin.gh",
#   "Version": "1.0.0",
#   "MinWoxVersion": "2.4.2",
#   "Runtime": "PYTHON",
#   "Description": "Jump straight to a GitHub repository, one of its pages, your fork of it, or your pull request and issue inboxes",
#   "Icon": "svg:<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' width='48' height='48'><path fill='var(--wox-theme-icon-color)' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z'/></svg>",
#   "TriggerKeywords": ["gh"],
#   "SupportedOS": ["Windows", "Darwin", "Linux"],
#   "Commands": [
#     { "Command": "pulls", "Description": "i18n:gh_cmd_pulls" },
#     { "Command": "issues", "Description": "i18n:gh_cmd_issues" },
#     { "Command": "notifications", "Description": "i18n:gh_cmd_notifications" },
#     { "Command": "gists", "Description": "i18n:gh_cmd_gists" },
#     { "Command": "refresh", "Description": "i18n:gh_cmd_refresh" }
#   ],
#   "SettingDefinitions": [
#     { "Type": "head", "Value": { "Content": "i18n:gh_head_cli" } },
#     {
#       "Type": "textbox",
#       "IsPlatformSpecific": true,
#       "Value": {
#         "Key": "ghPath",
#         "Label": "i18n:gh_setting_gh_path",
#         "DefaultValue": "gh",
#         "Tooltip": "i18n:gh_setting_gh_path_tooltip",
#         "MaxLines": 1,
#         "Validators": [{ "Type": "not_empty", "Value": {} }],
#         "Style": { "Width": 360 }
#       }
#     },
#     { "Type": "head", "Value": { "Content": "i18n:gh_head_cache" } },
#     {
#       "Type": "textbox",
#       "Value": {
#         "Key": "cacheTtlHours",
#         "Label": "i18n:gh_setting_ttl",
#         "DefaultValue": "24",
#         "Tooltip": "i18n:gh_setting_ttl_tooltip",
#         "MaxLines": 1,
#         "Suffix": "h",
#         "Validators": [{ "Type": "is_number", "Value": { "IsInteger": true, "IsFloat": false } }],
#         "Style": { "Width": 120 }
#       }
#     },
#     {
#       "Type": "checkbox",
#       "Value": {
#         "Key": "includeArchived",
#         "Label": "i18n:gh_setting_include_archived",
#         "DefaultValue": "false",
#         "Tooltip": "i18n:gh_setting_include_archived_tooltip"
#       }
#     },
#     {
#       "Type": "checkbox",
#       "Value": {
#         "Key": "registerRepoCommands",
#         "Label": "i18n:gh_setting_repo_commands",
#         "DefaultValue": "false",
#         "Tooltip": "i18n:gh_setting_repo_commands_tooltip"
#       }
#     }
#   ],
#   "I18n": {
#     "en_US": {
#       "gh_cmd_pulls": "Pull requests that involve you",
#       "gh_cmd_issues": "Issues that involve you",
#       "gh_cmd_notifications": "Your notification inbox",
#       "gh_cmd_gists": "Your gists",
#       "gh_cmd_refresh": "Rebuild the repository autocomplete cache",
#       "gh_head_cli": "GitHub CLI",
#       "gh_head_cache": "Repository cache",
#       "gh_setting_gh_path": "gh executable",
#       "gh_setting_gh_path_tooltip": "Path to the GitHub CLI. The plugin runs 'gh auth token' to authenticate, so no token is stored in Wox.",
#       "gh_setting_ttl": "Refresh after",
#       "gh_setting_ttl_tooltip": "How old the cached repository list may get before it is refreshed in the background.",
#       "gh_setting_include_archived": "Include archived repositories",
#       "gh_setting_include_archived_tooltip": "Show archived repositories in autocomplete results.",
#       "gh_setting_repo_commands": "Register repository names for inline Tab completion",
#       "gh_setting_repo_commands_tooltip": "Also expose cached repository names as query commands. This enables Wox inline Tab completion, but adds one entry per repository to global search."
#     },
#     "zh_CN": {
#       "gh_cmd_pulls": "与你相关的拉取请求",
#       "gh_cmd_issues": "与你相关的议题",
#       "gh_cmd_notifications": "你的通知收件箱",
#       "gh_cmd_gists": "你的代码片段",
#       "gh_cmd_refresh": "重建仓库自动补全缓存",
#       "gh_head_cli": "GitHub CLI",
#       "gh_head_cache": "仓库缓存",
#       "gh_setting_gh_path": "gh 可执行文件",
#       "gh_setting_gh_path_tooltip": "GitHub CLI 的路径。插件通过运行 'gh auth token' 获取凭据，不会在 Wox 中保存令牌。",
#       "gh_setting_ttl": "刷新间隔",
#       "gh_setting_ttl_tooltip": "缓存的仓库列表超过该时长后会在后台刷新。",
#       "gh_setting_include_archived": "包含已归档的仓库",
#       "gh_setting_include_archived_tooltip": "在自动补全结果中显示已归档的仓库。",
#       "gh_setting_repo_commands": "将仓库名注册为可 Tab 补全的命令",
#       "gh_setting_repo_commands_tooltip": "把缓存的仓库名同时注册为查询命令，从而启用 Wox 行内 Tab 补全，但会在全局搜索中为每个仓库增加一个条目。"
#     }
#   }
# }

"""
GitHub Jump — a single-file Wox SDK plugin.

Query grammar (trigger keyword ``gh``)::

    gh                                  shortcuts + your most recently pushed repositories
    gh pyst                             fuzzy match against cached repository names
    gh danudey/pystrptime               open that repository
    gh danudey/pystrptime releases      open that repository's releases page
    gh danudey/pystrptime fork          open your fork of that repository
    gh pulls                            your pull request inbox
    gh refresh                          rebuild the repository cache now

Authentication reuses the GitHub CLI: the plugin shells out to ``gh auth token``
and never stores a token of its own. Navigation to an explicitly typed
``owner/repo`` works without any authentication; only autocomplete and fork
resolution need it.

Everything here is standard library plus the Wox Python SDK, so the file can be
dropped into ``~/.wox/wox-user/plugins/single-file/`` as-is.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from typing import Any, Dict, List, Optional, Sequence, Tuple

from wox_plugin import (
    ActionContext,
    ChangeQueryParam,
    Context,
    CopyParams,
    CopyType,
    LogLevel,
    MetadataCommand,
    PluginInitParams,
    Query,
    QueryResponse,
    QueryType,
    RefreshQueryParam,
    Result,
    ResultAction,
    ResultTail,
    ResultTailTextCategory,
    ResultTailType,
    WoxImage,
    WoxPreview,
    WoxPreviewType,
)

GITHUB = "https://github.com"
GIST = "https://gist.github.com"
API = "https://api.github.com"
API_VERSION = "2022-11-28"
USER_AGENT = "Wox.Plugin.gh"

REPO_SPEC_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*$")

# Result identity may be colourful; this mark is monochrome so it stays legible
# in both light and dark themes.
ICON_GITHUB = WoxImage.new_svg(
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' width='48' height='48'>"
    "<path fill='var(--wox-theme-icon-color)' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 "
    "0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 "
    "1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 "
    "0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 "
    "0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z'/></svg>"
)

# Action Panel glyphs must be monochrome and theme adaptive, mirroring Wox's
# built-in action.* catalog.
_ACTION_SVG_HEAD = (
    "<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' "
    "stroke='var(--wox-theme-icon-color)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>"
)
ICON_OPEN = WoxImage.new_svg(_ACTION_SVG_HEAD + "<path d='M14 5h5v5M19 5l-9 9'/><path d='M13 7H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-7'/></svg>")
ICON_COPY = WoxImage.new_svg(_ACTION_SVG_HEAD + "<rect x='8' y='8' width='12' height='12' rx='2'/><path d='M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2'/></svg>")
ICON_EXECUTE = WoxImage.new_svg(_ACTION_SVG_HEAD + "<path d='M13 2 4.5 13.5h5.5L9 22l10-13h-6z'/></svg>")
ICON_SEARCH = WoxImage.new_svg(_ACTION_SVG_HEAD + "<circle cx='11' cy='11' r='7'/><path d='m20 20-4-4'/></svg>")

# key, label, path suffix (None marks a computed page), extra search aliases
SUBPAGES: Sequence[Tuple[str, str, Optional[str], Sequence[str]]] = (
    ("code", "Code", "", ("repo", "home", "source", "files", "root")),
    ("issues", "Issues", "/issues", ("bugs",)),
    ("pulls", "Pull requests", "/pulls", ("pr", "prs", "pull", "reviews")),
    ("releases", "Releases", "/releases", ("release", "downloads", "changelog")),
    ("actions", "Actions", "/actions", ("ci", "workflows", "builds")),
    ("commits", "Commits", "/commits", ("log", "history")),
    ("branches", "Branches", "/branches", ()),
    ("tags", "Tags", "/tags", ()),
    ("discussions", "Discussions", "/discussions", ("forum",)),
    ("wiki", "Wiki", "/wiki", ("docs",)),
    ("insights", "Insights", "/pulse", ("pulse", "graphs", "stats", "contributors")),
    ("security", "Security", "/security", ("advisories", "dependabot", "vulnerabilities")),
    ("network", "Forks", "/forks", ("network",)),
    ("stargazers", "Stargazers", "/stargazers", ("stars",)),
    ("settings", "Settings", "/settings", ("config", "admin")),
    ("fork", "My fork", None, ("myfork", "forked")),
)

# key, title, subtitle, url template, extra aliases. {login} is filled in when
# the GitHub CLI has told us who we are.
SHORTCUTS: Sequence[Tuple[str, str, str, str, Sequence[str]]] = (
    ("pulls", "Pull requests", "Pull requests that involve you", GITHUB + "/pulls", ("prs", "pr", "pull", "reviews")),
    ("issues", "Issues", "Issues that involve you", GITHUB + "/issues", ("issue",)),
    ("notifications", "Notifications", "Your notification inbox", GITHUB + "/notifications", ("notifs", "inbox", "bell")),
    ("gists", "Gists", "Your gists", GIST + "/{login}", ("gist", "snippets")),
    ("stars", "Starred", "Repositories you starred", GITHUB + "/{login}?tab=stars", ("starred", "favourites", "favorites")),
    ("profile", "Your profile", "github.com/{login}", GITHUB + "/{login}", ("me", "home")),
    ("new", "New repository", "Create a repository", GITHUB + "/new", ("create",)),
    ("explore", "Explore", "Explore GitHub", GITHUB + "/explore", ("trending", "discover")),
)

# Wox rewrites Ctrl to Command on macOS, so one spelling covers every platform.
BROWSE_HOTKEY = "Ctrl+B"
FORK_MEMO_TTL = 600.0


def fuzzy_score(needle: str, haystack: str) -> int:
    """Rank ``haystack`` against ``needle``. Zero means no match."""
    if not needle:
        return 1
    n = needle.lower()
    h = haystack.lower()
    if not h:
        return 0
    if n == h:
        return 1000
    index = h.find(n)
    if index == 0:
        return 850 - min(len(h) - len(n), 100)
    if index > 0:
        boundary = 60 if h[index - 1] in "/-_. " else 0
        return 700 + boundary - min(index, 60) - min(len(h) - len(n), 40)

    position = 0
    gaps = 0
    last = -1
    for char in n:
        found = h.find(char, position)
        if found < 0:
            return 0
        if last >= 0 and found != last + 1:
            gaps += 1
        last = found
        position = found + 1
    return max(120, 400 - gaps * 25 - min(len(h), 60))


def score_repo(needle: str, full_name: str, name: str) -> int:
    """Score a repository, preferring a hit on the bare name over the owner."""
    if not needle:
        return 1
    if "/" in needle:
        return fuzzy_score(needle, full_name)
    by_name = fuzzy_score(needle, name)
    return max(by_name + 60 if by_name else 0, fuzzy_score(needle, full_name))


def open_url_sync(url: str) -> None:
    """Hand a URL to the desktop browser without blocking the runtime host."""
    try:
        if sys.platform == "darwin":
            subprocess.Popen(["open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            return
        if os.name == "nt":
            os.startfile(url)  # type: ignore[attr-defined]
            return
        subprocess.Popen(
            ["xdg-open", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        return
    except (OSError, AttributeError):
        pass
    webbrowser.open(url)


def parse_next_link(link_header: str) -> Optional[str]:
    """Pull the rel="next" URL out of a GitHub Link header."""
    for part in link_header.split(","):
        section = part.split(";")
        if len(section) < 2:
            continue
        url = section[0].strip()
        if not url.startswith("<") or not url.endswith(">"):
            continue
        for attribute in section[1:]:
            if attribute.strip() in ('rel="next"', "rel=next"):
                return url[1:-1]
    return None


def http_json(url: str, token: Optional[str], timeout: float = 20.0) -> Tuple[Any, str]:
    """GET a GitHub API URL and return (decoded body, Link header)."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
        link = response.headers.get("Link", "") or ""
    return json.loads(body) if body else None, link


class GitHubJumpPlugin:
    def __init__(self) -> None:
        self.api: Any = None
        self.cache_folder: str = ""
        self.cache_path: str = ""
        self._repos: List[Dict[str, Any]] = []
        self._login: str = ""
        self._fetched_at: float = 0.0
        self._token: Optional[str] = None
        self._token_checked_at: float = 0.0
        self._token_error: str = ""
        self._refresh_lock: Optional[asyncio.Lock] = None
        self._refreshing: bool = False
        self._last_refresh_error: str = ""
        self._fork_memo: Dict[str, Tuple[float, Optional[str]]] = {}
        self._fork_pending: Dict[str, bool] = {}
        self._registered_repo_commands: bool = False
        self._include_archived_cached: bool = False

    # ------------------------------------------------------------------
    # lifecycle
    # ------------------------------------------------------------------

    async def init(self, ctx: Context, params: PluginInitParams) -> None:
        self.api = params.api
        self._refresh_lock = asyncio.Lock()
        self.cache_folder = await self.api.get_cache_folder(ctx)
        self.cache_path = os.path.join(self.cache_folder, "repos.json")
        await self._load_cache_file(ctx)
        await self.api.on_setting_changed(ctx, self._on_setting_changed)
        await self.api.on_unload(ctx, self._on_unload)
        asyncio.create_task(self._refresh_if_stale(ctx))

    async def _on_unload(self, ctx: Context) -> None:
        self._fork_memo.clear()
        self._fork_pending.clear()

    async def _on_setting_changed(self, ctx: Context, key: str, value: str) -> None:
        if key == "ghPath":
            self._token = None
            self._token_checked_at = 0.0
            self._token_error = ""
            asyncio.create_task(self._refresh_repos(ctx, force=True))
        elif key == "registerRepoCommands":
            await self._sync_repo_commands(ctx)
        elif key == "cacheTtlHours":
            asyncio.create_task(self._refresh_if_stale(ctx))

    async def _log(self, ctx: Context, level: LogLevel, message: str) -> None:
        try:
            await self.api.log(ctx, level, message)
        except Exception:  # logging must never break a query
            pass

    # ------------------------------------------------------------------
    # settings
    # ------------------------------------------------------------------

    async def _setting(self, ctx: Context, key: str, default: str = "") -> str:
        try:
            value = await self.api.get_setting(ctx, key)
        except Exception:
            return default
        return value if value else default

    async def _gh_path(self, ctx: Context) -> str:
        return await self._setting(ctx, "ghPath", "gh")

    async def _cache_ttl_seconds(self, ctx: Context) -> float:
        raw = await self._setting(ctx, "cacheTtlHours", "24")
        try:
            hours = float(raw)
        except ValueError:
            hours = 24.0
        return max(hours, 0.0) * 3600.0

    async def _include_archived(self, ctx: Context) -> bool:
        return (await self._setting(ctx, "includeArchived", "false")).lower() == "true"

    async def _repo_commands_enabled(self, ctx: Context) -> bool:
        return (await self._setting(ctx, "registerRepoCommands", "false")).lower() == "true"

    # ------------------------------------------------------------------
    # authentication
    # ------------------------------------------------------------------

    def _read_token_sync(self, gh_path: str) -> Tuple[Optional[str], str]:
        try:
            completed = subprocess.run(
                [gh_path, "auth", "token"],
                capture_output=True,
                text=True,
                timeout=15,
            )
        except FileNotFoundError:
            return None, "GitHub CLI not found at '%s'." % gh_path
        except subprocess.TimeoutExpired:
            return None, "'%s auth token' timed out." % gh_path
        except OSError as error:
            return None, "Could not run '%s auth token': %s" % (gh_path, error)

        token = completed.stdout.strip()
        if completed.returncode != 0 or not token:
            detail = completed.stderr.strip() or "no token returned"
            return None, "GitHub CLI is not authenticated (%s)." % detail
        return token, ""

    async def _token_for(self, ctx: Context) -> Optional[str]:
        """Return a cached gh token, re-reading it at most every five minutes."""
        now = time.time()
        if self._token and now - self._token_checked_at < 300:
            return self._token
        if not self._token and self._token_error and now - self._token_checked_at < 60:
            return None

        gh_path = await self._gh_path(ctx)
        token, error = await asyncio.to_thread(self._read_token_sync, gh_path)
        self._token = token
        self._token_error = error
        self._token_checked_at = now
        if error:
            await self._log(ctx, LogLevel.INFO, "gh auth: " + error)
        return token

    # ------------------------------------------------------------------
    # repository cache
    # ------------------------------------------------------------------

    async def _load_cache_file(self, ctx: Context) -> None:
        try:
            raw = await asyncio.to_thread(self._read_cache_sync)
        except Exception as error:
            await self._log(ctx, LogLevel.ERROR, "could not read repo cache: %s" % error)
            return
        if not raw:
            return
        self._repos = raw.get("repos", []) or []
        self._login = raw.get("login", "") or ""
        self._fetched_at = float(raw.get("fetched_at", 0) or 0)

    def _read_cache_sync(self) -> Optional[Dict[str, Any]]:
        if not self.cache_path or not os.path.exists(self.cache_path):
            return None
        with open(self.cache_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def _write_cache_sync(self, payload: Dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
        temporary = self.cache_path + ".tmp"
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump(payload, handle)
        os.replace(temporary, self.cache_path)

    def _fetch_repos_sync(self, token: str) -> Tuple[str, List[Dict[str, Any]]]:
        """Fetch the viewer's login plus every repo they own or share via an org."""
        viewer, _ = http_json(API + "/user", token)
        login = (viewer or {}).get("login", "")

        repos: List[Dict[str, Any]] = []
        url: Optional[str] = (
            API + "/user/repos?per_page=100&sort=full_name&affiliation=owner,organization_member"
        )
        pages = 0
        while url and pages < 30:
            payload, link = http_json(url, token)
            for repo in payload or []:
                repos.append(
                    {
                        "full_name": repo.get("full_name", ""),
                        "name": repo.get("name", ""),
                        "owner": (repo.get("owner") or {}).get("login", ""),
                        "description": repo.get("description") or "",
                        "private": bool(repo.get("private")),
                        "fork": bool(repo.get("fork")),
                        "archived": bool(repo.get("archived")),
                        "pushed_at": repo.get("pushed_at") or "",
                        "html_url": repo.get("html_url") or "",
                        "default_branch": repo.get("default_branch") or "main",
                        "language": repo.get("language") or "",
                        "stars": int(repo.get("stargazers_count") or 0),
                    }
                )
            pages += 1
            url = parse_next_link(link)
        return login, repos

    async def _refresh_if_stale(self, ctx: Context) -> None:
        ttl = await self._cache_ttl_seconds(ctx)
        if self._repos and ttl > 0 and time.time() - self._fetched_at < ttl:
            await self._sync_repo_commands(ctx)
            return
        await self._refresh_repos(ctx, force=False)

    async def _refresh_repos(self, ctx: Context, force: bool) -> bool:
        if self._refresh_lock is None:
            self._refresh_lock = asyncio.Lock()
        if self._refreshing and not force:
            return False
        async with self._refresh_lock:
            self._refreshing = True
            try:
                token = await self._token_for(ctx)
                if not token:
                    self._last_refresh_error = self._token_error
                    return False
                login, repos = await asyncio.to_thread(self._fetch_repos_sync, token)
                self._repos = repos
                self._login = login
                self._fetched_at = time.time()
                self._last_refresh_error = ""
                self._fork_memo.clear()
                await asyncio.to_thread(
                    self._write_cache_sync,
                    {"fetched_at": self._fetched_at, "login": login, "repos": repos},
                )
                await self._log(ctx, LogLevel.INFO, "cached %d repositories for %s" % (len(repos), login or "?"))
                await self._sync_repo_commands(ctx)
                return True
            except urllib.error.HTTPError as error:
                self._last_refresh_error = "GitHub API returned %s" % error.code
            except Exception as error:  # network, JSON, disk
                self._last_refresh_error = str(error)
            finally:
                self._refreshing = False
        await self._log(ctx, LogLevel.ERROR, "repo refresh failed: " + self._last_refresh_error)
        return False

    async def _sync_repo_commands(self, ctx: Context) -> None:
        """Optionally expose repo names as query commands for inline Tab completion."""
        enabled = await self._repo_commands_enabled(ctx)
        if not enabled:
            if self._registered_repo_commands:
                try:
                    await self.api.register_query_commands(ctx, [])
                except Exception:
                    pass
                self._registered_repo_commands = False
            return

        ordered = sorted(self._repos, key=lambda repo: repo.get("pushed_at", ""), reverse=True)
        commands = [
            MetadataCommand(command=repo["full_name"], description=repo.get("description") or "GitHub repository")
            for repo in ordered[:500]
            if repo.get("full_name")
        ]
        try:
            await self.api.register_query_commands(ctx, commands)
            self._registered_repo_commands = True
        except Exception as error:
            await self._log(ctx, LogLevel.ERROR, "could not register repo commands: %s" % error)

    # ------------------------------------------------------------------
    # fork resolution
    # ------------------------------------------------------------------

    def _resolve_fork_sync(self, token: Optional[str], owner: str, repo: str, candidates: Sequence[str]) -> Optional[str]:
        target = ("%s/%s" % (owner, repo)).lower()
        for candidate_owner in candidates:
            if not candidate_owner or candidate_owner.lower() == owner.lower():
                continue
            url = "%s/repos/%s/%s" % (API, urllib.parse.quote(candidate_owner), urllib.parse.quote(repo))
            try:
                payload, _ = http_json(url, token, timeout=8.0)
            except Exception:
                continue
            if not payload or not payload.get("fork"):
                continue
            parent = (payload.get("parent") or {}).get("full_name", "")
            source = (payload.get("source") or {}).get("full_name", "")
            if parent.lower() == target or source.lower() == target:
                return payload.get("html_url") or "%s/%s/%s" % (GITHUB, candidate_owner, repo)
        return None

    def _lookup_fork(self, owner: str, repo: str) -> Tuple[str, Optional[str]]:
        """Return (state, url) where state is 'known', 'pending' or 'unknown'."""
        key = ("%s/%s" % (owner, repo)).lower()
        cached = self._fork_memo.get(key)
        if cached and time.time() - cached[0] < FORK_MEMO_TTL:
            return "known", cached[1]
        if self._fork_pending.get(key):
            return "pending", None
        return "unknown", None

    async def _resolve_fork_background(self, ctx: Context, owner: str, repo: str) -> None:
        """Resolve a fork off the query path, then ask Wox to re-run the query."""
        key = ("%s/%s" % (owner, repo)).lower()
        if self._fork_pending.get(key):
            return
        self._fork_pending[key] = True
        try:
            token = await self._token_for(ctx)
            candidates: List[str] = []
            # A fork usually keeps the upstream name, so cached entries under any
            # of our owners are the cheapest place to look first.
            for entry in self._repos:
                if entry.get("name", "").lower() == repo.lower() and entry.get("fork"):
                    candidates.append(entry.get("owner", ""))
            if self._login and self._login not in candidates:
                candidates.append(self._login)

            url: Optional[str] = None
            if candidates:
                url = await asyncio.to_thread(self._resolve_fork_sync, token, owner, repo, candidates[:4])
            self._fork_memo[key] = (time.time(), url)
        except Exception as error:
            self._fork_memo[key] = (time.time(), None)
            await self._log(ctx, LogLevel.ERROR, "fork lookup failed for %s/%s: %s" % (owner, repo, error))
        finally:
            self._fork_pending.pop(key, None)

        try:
            await self.api.refresh_query(ctx, RefreshQueryParam(preserve_selected_index=True))
        except Exception:
            pass

    # ------------------------------------------------------------------
    # actions
    # ------------------------------------------------------------------

    def _open_action(self, url: str, name: str = "Open in browser", default: bool = True) -> ResultAction:
        async def _run(ctx: Context, action_ctx: ActionContext) -> None:
            await asyncio.to_thread(open_url_sync, url)

        return ResultAction(name=name, icon=ICON_OPEN, is_default=default, action=_run)

    def _copy_action(self, text: str, name: str, hotkey: str = "") -> ResultAction:
        async def _run(ctx: Context, action_ctx: ActionContext) -> None:
            await self.api.copy(ctx, CopyParams(type=CopyType.TEXT, text=text))

        return ResultAction(name=name, icon=ICON_COPY, hotkey=hotkey, action=_run)

    def _drill_action(self, full_name: str, trigger: str) -> ResultAction:
        completion = "%s %s " % (trigger, full_name)

        async def _run(ctx: Context, action_ctx: ActionContext) -> None:
            await self.api.change_query(
                ctx,
                ChangeQueryParam(query_type=QueryType.INPUT, query_text=completion),
            )

        return ResultAction(
            name="Browse pages",
            icon=ICON_SEARCH,
            hotkey=BROWSE_HOTKEY,
            prevent_hide_after_action=True,
            search_aliases=["autocomplete", "complete", "subpage", "drill"],
            action=_run,
        )

    def _refresh_action(self) -> ResultAction:
        async def _run(ctx: Context, action_ctx: ActionContext) -> None:
            await self.api.notify(ctx, "Refreshing GitHub repository cache…")
            if await self._refresh_repos(ctx, force=True):
                await self.api.notify(ctx, "Cached %d GitHub repositories." % len(self._repos))
            else:
                await self.api.notify(ctx, "Refresh failed: " + (self._last_refresh_error or "unknown error"))

        return ResultAction(name="Refresh now", icon=ICON_EXECUTE, is_default=True, prevent_hide_after_action=True, action=_run)

    # ------------------------------------------------------------------
    # result builders
    # ------------------------------------------------------------------

    def _repo_preview(self, repo: Dict[str, Any]) -> WoxPreview:
        lines = ["## %s" % repo.get("full_name", "")]
        if repo.get("description"):
            lines.append("")
            lines.append(repo["description"])
        facts = []
        if repo.get("private"):
            facts.append("private")
        if repo.get("fork"):
            facts.append("fork")
        if repo.get("archived"):
            facts.append("archived")
        if repo.get("language"):
            facts.append(repo["language"])
        if repo.get("stars"):
            facts.append("★ %d" % repo["stars"])
        if repo.get("default_branch"):
            facts.append("default branch `%s`" % repo["default_branch"])
        if facts:
            lines.append("")
            lines.append(" · ".join(facts))
        if repo.get("pushed_at"):
            lines.append("")
            lines.append("Last push %s" % repo["pushed_at"].replace("T", " ").replace("Z", " UTC"))
        return WoxPreview(preview_type=WoxPreviewType.MARKDOWN, preview_data="\n".join(lines))

    def _repo_tails(self, repo: Dict[str, Any]) -> List[ResultTail]:
        tails: List[ResultTail] = []
        if repo.get("private"):
            tails.append(ResultTail(type=ResultTailType.TEXT, text="private", text_category=ResultTailTextCategory.WARNING))
        if repo.get("archived"):
            tails.append(ResultTail(type=ResultTailType.TEXT, text="archived", text_category=ResultTailTextCategory.DANGER))
        if repo.get("fork"):
            tails.append(ResultTail(type=ResultTailType.TEXT, text="fork"))
        return tails

    def _repo_result(self, repo: Dict[str, Any], trigger: str, score: float) -> Result:
        full_name = repo.get("full_name", "")
        url = repo.get("html_url") or "%s/%s" % (GITHUB, full_name)
        owner = repo.get("owner", "") or full_name.split("/")[0]
        name = repo.get("name", "") or full_name.split("/")[-1]
        return Result(
            id="repo:" + full_name,
            title=full_name,
            sub_title=repo.get("description") or url,
            icon=ICON_GITHUB,
            score=score,
            score_key="repo:" + full_name,
            preview=self._repo_preview(repo),
            tails=self._repo_tails(repo),
            actions=[
                self._open_action(url),
                self._drill_action(full_name, trigger),
                self._open_action(url + "/issues", "Open issues", default=False),
                self._open_action(url + "/pulls", "Open pull requests", default=False),
                self._copy_action(url, "Copy URL"),
                self._copy_action("git clone git@github.com:%s/%s.git" % (owner, name), "Copy SSH clone command"),
            ],
        )

    def _bare_repo_result(self, spec: str, trigger: str, score: float) -> Result:
        owner, _, name = spec.partition("/")
        url = "%s/%s/%s" % (GITHUB, owner, name)
        return Result(
            id="repo:" + spec,
            title=spec,
            sub_title=url,
            icon=ICON_GITHUB,
            score=score,
            score_key="repo:" + spec,
            actions=[
                self._open_action(url),
                self._drill_action(spec, trigger),
                self._copy_action(url, "Copy URL"),
                self._copy_action("git clone git@github.com:%s/%s.git" % (owner, name), "Copy SSH clone command"),
            ],
        )

    def _url_result(self, result_id: str, title: str, subtitle: str, url: str, score: float) -> Result:
        return Result(
            id=result_id,
            title=title,
            sub_title=subtitle,
            icon=ICON_GITHUB,
            score=score,
            score_key=result_id,
            actions=[self._open_action(url), self._copy_action(url, "Copy URL")],
        )

    def _setup_result(self, message: str) -> Result:
        return Result(
            id="gh:setup",
            title="GitHub CLI is not ready",
            sub_title=message + "  Run 'gh auth login', then press Enter here to retry.",
            icon=ICON_GITHUB,
            score=900,
            actions=[
                ResultAction(
                    name="Retry",
                    icon=ICON_EXECUTE,
                    is_default=True,
                    prevent_hide_after_action=True,
                    action=self._retry_auth,
                ),
                self._copy_action("gh auth login", "Copy 'gh auth login'"),
            ],
        )

    async def _retry_auth(self, ctx: Context, action_ctx: ActionContext) -> None:
        self._token = None
        self._token_checked_at = 0.0
        self._token_error = ""
        if await self._refresh_repos(ctx, force=True):
            await self.api.notify(ctx, "Cached %d GitHub repositories." % len(self._repos))
        else:
            await self.api.notify(ctx, self._last_refresh_error or "Still not authenticated.")

    # ------------------------------------------------------------------
    # query
    # ------------------------------------------------------------------

    @staticmethod
    def _full_search(query: Query) -> str:
        """Rebuild the text after the trigger keyword, command splitting aside."""
        parts = [part for part in (query.command, query.search) if part]
        return " ".join(parts).strip()

    async def query(self, ctx: Context, query: Query) -> QueryResponse:
        trigger = query.trigger_keyword or "gh"
        self._include_archived_cached = await self._include_archived(ctx)
        search = self._full_search(query)
        tokens = search.split()
        trailing_space = query.raw_query.endswith(" ") and bool(tokens)

        if tokens and "/" in tokens[0] and (len(tokens) > 1 or trailing_space):
            results = await self._repo_page_results(ctx, trigger, tokens[0], " ".join(tokens[1:]))
        else:
            results = await self._top_level_results(ctx, trigger, search)

        # An explicitly typed owner/repo can also come back from the fuzzy pass,
        # so collapse duplicates on result id and keep the better score.
        best: Dict[str, Result] = {}
        for result in results:
            existing = best.get(result.id)
            if existing is None or result.score > existing.score:
                best[result.id] = result
        deduped = list(best.values())
        deduped.sort(key=lambda item: item.score, reverse=True)
        return QueryResponse(results=deduped)

    async def _top_level_results(self, ctx: Context, trigger: str, search: str) -> List[Result]:
        results: List[Result] = []
        lowered = search.lower()

        refresh_score = 0.0
        if lowered in ("refresh", "reload", "sync"):
            refresh_score = 985.0
        elif len(lowered) >= 2 and ("refresh".startswith(lowered) or "reload".startswith(lowered) or "sync".startswith(lowered)):
            refresh_score = 400.0 + 80.0 * len(lowered)
        elif not lowered:
            refresh_score = 300.0
        if refresh_score:
            results.append(
                Result(
                    id="gh:refresh",
                    title="Refresh repository cache",
                    sub_title=self._cache_summary(),
                    icon=ICON_GITHUB,
                    score=min(refresh_score, 985.0),
                    score_key="gh:refresh",
                    actions=[self._refresh_action()],
                )
            )

        # An explicitly typed owner/repo always wins, cached or not.
        if REPO_SPEC_RE.match(search):
            known = self._find_repo(search)
            if known:
                results.append(self._repo_result(known, trigger, 990))
            else:
                results.append(self._bare_repo_result(search, trigger, 990))

        results.extend(await self._shortcut_results(ctx, search))
        results.extend(self._repo_matches(search, trigger))

        if search and not REPO_SPEC_RE.match(search):
            encoded = urllib.parse.quote(search)
            results.append(
                self._url_result(
                    "gh:search",
                    "Search GitHub for “%s”" % search,
                    "%s/search?q=%s&type=repositories" % (GITHUB, encoded),
                    "%s/search?q=%s&type=repositories" % (GITHUB, encoded),
                    50,
                )
            )

        if not self._repos:
            # Navigation still works unauthenticated; only autocomplete needs a
            # token, so this stays a hint rather than a QueryRequirement block.
            token = await self._token_for(ctx)
            if not token:
                results.append(self._setup_result(self._token_error))
        return results

    def _cache_summary(self) -> str:
        if not self._repos:
            return self._last_refresh_error or "No repositories cached yet."
        age = time.time() - self._fetched_at
        if age < 90:
            when = "just now"
        elif age < 3600:
            when = "%d minutes ago" % (age // 60)
        elif age < 86400:
            when = "%d hours ago" % (age // 3600)
        else:
            when = "%d days ago" % (age // 86400)
        return "%d repositories, cached %s" % (len(self._repos), when)

    def _find_repo(self, full_name: str) -> Optional[Dict[str, Any]]:
        lowered = full_name.lower()
        for repo in self._repos:
            if repo.get("full_name", "").lower() == lowered:
                return repo
        return None

    async def _shortcut_results(self, ctx: Context, search: str) -> List[Result]:
        results: List[Result] = []
        for key, title, subtitle, template, aliases in SHORTCUTS:
            if "{login}" in template and not self._login:
                continue
            score = max([fuzzy_score(search, key)] + [fuzzy_score(search, alias) for alias in aliases])
            if not score:
                continue
            url = template.format(login=urllib.parse.quote(self._login))
            results.append(
                self._url_result(
                    "gh:" + key,
                    title,
                    subtitle.format(login=self._login),
                    url,
                    # Keep shortcuts above fuzzy repo noise but below an exact
                    # owner/repo the user actually typed.
                    min(score + 120, 980) if search else 900 - len(results),
                )
            )
        return results

    def _repo_matches(self, search: str, trigger: str) -> List[Result]:
        if not self._repos:
            return []
        scored: List[Tuple[int, Dict[str, Any]]] = []
        for repo in self._repos:
            if repo.get("archived") and not self._include_archived_cached:
                continue
            full_name = repo.get("full_name", "")
            if not full_name:
                continue
            score = score_repo(search, full_name, repo.get("name", ""))
            if score:
                scored.append((score, repo))

        if not search:
            scored.sort(key=lambda item: item[1].get("pushed_at", ""), reverse=True)
            return [self._repo_result(repo, trigger, 400 - index) for index, (_, repo) in enumerate(scored[:12])]

        scored.sort(key=lambda item: (item[0], item[1].get("pushed_at", "")), reverse=True)
        return [self._repo_result(repo, trigger, min(score, 960)) for score, repo in scored[:30]]

    async def _repo_page_results(self, ctx: Context, trigger: str, spec: str, filter_text: str) -> List[Result]:
        owner, _, name = spec.partition("/")
        if not owner or not name:
            return await self._top_level_results(ctx, trigger, spec)

        base = "%s/%s/%s" % (GITHUB, urllib.parse.quote(owner), urllib.parse.quote(name))
        known = self._find_repo(spec)
        if known and known.get("html_url"):
            base = known["html_url"]

        results: List[Result] = []
        for key, label, suffix, aliases in SUBPAGES:
            score = max([fuzzy_score(filter_text, key), fuzzy_score(filter_text, label)] + [fuzzy_score(filter_text, alias) for alias in aliases])
            if not score:
                continue
            if key == "fork":
                results.append(await self._fork_result(ctx, owner, name, score))
                continue
            url = base + (suffix or "")
            results.append(
                Result(
                    id="page:%s:%s" % (spec, key),
                    title=label,
                    sub_title=url,
                    icon=ICON_GITHUB,
                    score=score if filter_text else 500 - len(results),
                    score_key="page:%s:%s" % (spec.lower(), key),
                    actions=[self._open_action(url), self._copy_action(url, "Copy URL")],
                )
            )

        if not results:
            encoded = urllib.parse.quote(filter_text)
            url = "%s/search?q=%s&type=code" % (base, encoded)
            results.append(
                self._url_result(
                    "page:%s:search" % spec,
                    "Search %s for “%s”" % (spec, filter_text),
                    url,
                    url,
                    100,
                )
            )
        return results

    async def _fork_result(self, ctx: Context, owner: str, name: str, score: float) -> Result:
        state, fork_url = self._lookup_fork(owner, name)
        create_url = "%s/%s/%s/fork" % (GITHUB, urllib.parse.quote(owner), urllib.parse.quote(name))
        result_id = "page:%s/%s:fork" % (owner, name)

        if state == "unknown":
            # Resolving needs the network, so keep it off the query path and let
            # the background task refresh the query once it knows.
            asyncio.create_task(self._resolve_fork_background(ctx, owner, name))

        if fork_url:
            return Result(
                id=result_id,
                title="My fork",
                sub_title=fork_url,
                icon=ICON_GITHUB,
                score=score,
                score_key=result_id,
                tails=[ResultTail(type=ResultTailType.TEXT, text="fork", text_category=ResultTailTextCategory.SUCCESS)],
                actions=[
                    self._open_action(fork_url),
                    self._open_action(fork_url + "/compare", "Open compare view", default=False),
                    self._copy_action(fork_url, "Copy URL"),
                ],
            )

        if state == "known":
            reason = "No fork found" if self._login else "Run 'gh auth login' so forks can be looked up"
        else:
            reason = "Looking for your fork…"
        return Result(
            id=result_id,
            title="Fork this repository",
            sub_title="%s — Enter opens %s" % (reason, create_url),
            icon=ICON_GITHUB,
            score=score,
            score_key=result_id,
            actions=[self._open_action(create_url, "Open fork page"), self._copy_action(create_url, "Copy URL")],
        )


plugin = GitHubJumpPlugin()
