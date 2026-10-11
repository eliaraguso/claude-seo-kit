"""Crawler tokens (for robots.txt) and user-agent strings (for fetching).

purpose: search · ai-training · ai-search · user-fetch · other
"""
from __future__ import annotations

BOT_TOKENS = [
    {"token": "Googlebot", "operator": "Google", "purpose": "search"},
    {"token": "Googlebot-Image", "operator": "Google", "purpose": "search"},
    {"token": "Googlebot-News", "operator": "Google", "purpose": "search"},
    {"token": "Google-Extended", "operator": "Google", "purpose": "ai-training"},
    {"token": "GoogleOther", "operator": "Google", "purpose": "other"},
    {"token": "Google-CloudVertexBot", "operator": "Google", "purpose": "other"},
    {"token": "Bingbot", "operator": "Microsoft", "purpose": "search"},
    {"token": "Applebot", "operator": "Apple", "purpose": "search"},
    {"token": "Applebot-Extended", "operator": "Apple", "purpose": "ai-training"},
    {"token": "GPTBot", "operator": "OpenAI", "purpose": "ai-training"},
    {"token": "ChatGPT-User", "operator": "OpenAI", "purpose": "user-fetch"},
    {"token": "OAI-SearchBot", "operator": "OpenAI", "purpose": "ai-search"},
    {"token": "ClaudeBot", "operator": "Anthropic", "purpose": "ai-training"},
    {"token": "Claude-User", "operator": "Anthropic", "purpose": "user-fetch"},
    {"token": "Claude-SearchBot", "operator": "Anthropic", "purpose": "ai-search"},
    {"token": "anthropic-ai", "operator": "Anthropic", "purpose": "ai-training"},
    {"token": "PerplexityBot", "operator": "Perplexity", "purpose": "ai-search"},
    {"token": "Perplexity-User", "operator": "Perplexity", "purpose": "user-fetch"},
    {"token": "Amazonbot", "operator": "Amazon", "purpose": "other"},
    {"token": "Bytespider", "operator": "ByteDance", "purpose": "ai-training"},
    {"token": "CCBot", "operator": "Common Crawl", "purpose": "ai-training"},
    {"token": "meta-externalagent", "operator": "Meta", "purpose": "ai-training"},
    {"token": "DuckAssistBot", "operator": "DuckDuckGo", "purpose": "ai-search"},
    {"token": "YandexBot", "operator": "Yandex", "purpose": "search"},
]

TOKENS = [b["token"] for b in BOT_TOKENS]

# Crawlers that obey a more generic group when no group names them (Google documents
# that Googlebot-Image and Googlebot-News fall back to the Googlebot group).
ROBOTS_FALLBACK = {
    "googlebot-image": ["googlebot"],
    "googlebot-news": ["googlebot"],
    "googlebot-video": ["googlebot"],
}

_CHROME = "Chrome/141.0.0.0"
USER_AGENTS = {
    "browser": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {_CHROME} Safari/537.36",
    "googlebot": ("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 "
                  f"(KHTML, like Gecko) {_CHROME} Mobile Safari/537.36 "
                  "(compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    "googlebot-desktop": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; "
                          f"+http://www.google.com/bot.html) {_CHROME} Safari/537.36"),
    "bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "oai-searchbot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; "
                      "+https://openai.com/searchbot"),
    "gptbot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.2; "
               "+https://openai.com/gptbot"),
    "chatgpt-user": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; "
                     "+https://openai.com/bot"),
    "claude-searchbot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; "
                         "+https://www.anthropic.com)"),
    "claudebot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; "
                  "+claudebot@anthropic.com)"),
    "claude-user": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; "
                    "+Claude-User@anthropic.com)"),
    "perplexitybot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; "
                      "+https://perplexity.ai/perplexitybot)"),
    "perplexity-user": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; "
                        "+https://perplexity.ai/perplexity-user)"),
    "applebot": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                 "Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)"),
    "duckassistbot": "DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)",
}

UA_SETS = {
    "default": ["browser", "googlebot", "bingbot", "oai-searchbot", "claude-searchbot", "perplexitybot"],
    "all": list(USER_AGENTS),
    "none": [],
}


def user_agent(name_or_string: str) -> str:
    """Map a short name ('googlebot') to its UA string; other strings pass through."""
    return USER_AGENTS.get((name_or_string or "").lower(), name_or_string or USER_AGENTS["browser"])
