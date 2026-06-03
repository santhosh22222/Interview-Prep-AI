import streamlit as st

DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --bg: #212121;
    --sidebar: #171717;
    --surface: #202123;
    --border: #2d2d2d;
    --text: #ececec;
    --text-muted: #b4b4b4;
    --accent: #10a37f;
    --accent-hover: #1a7f64;
    --hover: #2a2b32;
    --code-bg: #0d0d0d;
    --code-text: #e1e1e1;
    --shadow: rgba(0, 0, 0, 0.3);
    --user-bubble: #2f2f2f;
    --text2: #b4b4b4;
}

/* Global overrides */
body, .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}

[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] *,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] li,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] span,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] strong,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] em,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h1,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h3,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h4,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h5,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h6 {
    color: var(--text) !important;
}

[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] code,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] pre {
    color: var(--code-text) !important;
    background-color: var(--code-bg) !important;
}

label,
.stTextInput label,
.stTextArea label,
[data-testid="stWidgetLabel"] p {
    color: var(--text) !important;
}

/* Hide default Streamlit headers and footers */
[data-testid="stHeader"] {
    background-color: transparent !important;
    border-bottom: none !important;
}
footer {
    display: none !important;
    visibility: hidden !important;
}
#MainMenu {
    visibility: hidden !important;
}

/* Hide Default Sidebar Multi-page Navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Hide default Streamlit sidebar header globally to eliminate empty space at the top of the sidebar */
[data-testid="stSidebarHeader"],
div[class*="stSidebarHeader"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Sidebar Custom Styling */
[data-testid="stSidebar"] {
    background-color: var(--sidebar) !important;
    border-right: 1px solid var(--border) !important;
    width: 260px !important;
}
/* Eliminate the massive Streamlit default padding at the top of the sidebar and hide horizontal overflow */
[data-testid="stSidebarUserContent"] {
    padding-top: 6px !important;
    padding-bottom: 10px !important;
    overflow-x: hidden !important;
}
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    overflow-x: hidden !important;
}
@media (min-width: 768px) {
    /* Lock the sidebar permanently as a fixed panel on desktops, overriding collapse states */
    [data-testid="stSidebar"],
    section[data-testid="stSidebar"][data-collapsed="true"] {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        bottom: 0 !important;
        width: 260px !important;
        min-width: 260px !important;
        max-width: 260px !important;
        transform: translate3d(0, 0, 0) !important;
        transition: none !important;
        display: block !important;
        visibility: visible !important;
        z-index: 1000 !important;
    }
    /* Force the inner containers inside the sidebar to remain visible and fully open */
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] [data-testid="stSidebarUserContent"],
    section[data-testid="stSidebar"][data-collapsed="true"] > div,
    section[data-testid="stSidebar"][data-collapsed="true"] [data-testid="stSidebarUserContent"] {
        width: 260px !important;
        min-width: 260px !important;
        max-width: 260px !important;
        visibility: visible !important;
        display: block !important;
        opacity: 1 !important;
        transform: none !important;
    }
    /* Push main chat container to the right to make space for the fixed sidebar */
    .stMain, [data-testid="stMainBlockContainer"] {
        margin-left: 260px !important;
        width: calc(100% - 260px) !important;
        max-width: 100% !important;
    }
    /* Hide Streamlit collapse, expand and sidebar header containers to remove empty top space completely on desktops */
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapseButton"],
    button[data-testid="sidebar-collapse-button"],
    div[class*="collapsedControl"],
    [data-testid="stSidebarHeader"],
    div[class*="stSidebarHeader"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
}

[data-testid="stSidebar"] > div {
    background-color: var(--sidebar) !important;
}
[data-testid="stSidebar"] * {
    color: var(--text) !important;
}

/* Fixed Header Bar at the top of the main viewport */
.fixed-top-header {
    position: fixed !important;
    top: 0 !important;
    left: 260px !important;
    right: 0 !important;
    height: 56px !important;
    background-color: var(--bg) !important;
    border-bottom: 1px solid var(--border) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    padding: 0 24px !important;
    z-index: 998 !important;
}
@media (max-width: 768px) {
    .fixed-top-header {
        left: 0 !important;
    }
}

/* Push main chat container down and center content */
[data-testid="stMainBlockContainer"] {
    padding-top: 56px !important;
    padding-bottom: 30px !important;
    padding-left: 10% !important;
    padding-right: 10% !important;
    margin-top: 0 !important;
    max-width: 800px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
@media (max-width: 1200px) {
    [data-testid="stMainBlockContainer"] {
        padding-left: 5% !important;
        padding-right: 5% !important;
    }
}
@media (min-width: 768px) {
    [data-testid="stHeader"] {
        display: none !important;
    }
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="primary"] {
    background-color: var(--accent) !important;
    color: white !important;
    border: 1px solid var(--accent) !important;
    border-radius: 20px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 8px 16px !important;
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="secondary"] {
    background-color: var(--surface) !important;
    color: var(--text-muted) !important;
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 8px 16px !important;
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="secondary"]:hover {
    color: var(--text) !important;
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}


/* Chat messages full width within centered container */
[data-testid="stChatMessage"] {
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    background-color: transparent !important;
    border: none !important;
    padding: 0.5rem 0 !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
}
[data-testid="stChatMessage"] [data-testid="stAvatar"] {
    border-radius: 50% !important;
    border: 1px solid var(--border) !important;
    background-color: var(--surface) !important;
}

/* User message: right-aligned bubble */
[data-testid="stChatMessage"][data-testid*="user"],
[data-testid="stChatMessage"]:has(.chat-user-message) {
    flex-direction: row-reverse !important;
    justify-content: flex-start !important;
}
[data-testid="stChatMessage"]:has(.chat-user-message) [data-testid="stAvatar"] {
    display: none !important;
}
.chat-user-message {
    background-color: var(--user-bubble) !important;
    color: var(--text) !important;
    border-radius: 18px !important;
    padding: 10px 16px !important;
    display: block !important;
    max-width: 75% !important;
    margin-left: auto !important;
    margin-right: 0 !important;
    margin-bottom: 2px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    text-align: left !important;
}

/* Assistant message: left-aligned, no bubble */
.chat-assistant-message {
    color: var(--text) !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
    display: block !important;
    max-width: 100% !important;
}

/* Custom Chat Input styling - Exhaustive overrides */
[data-testid="stChatInput"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 26px !important;
    box-shadow: 0 4px 20px var(--shadow) !important;
    max-width: 100% !important;
    margin: 0 auto 10px auto !important;
    padding: 4px 12px !important;
}
/* Force all inner wrappers to be completely transparent to eliminate the dark rectangle */
[data-testid="stChatInput"] div,
[data-testid="stChatInput"] textarea {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--text) !important;
    font-size: 15px !important;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    outline: none !important;
}
/* Send button inside input styled as a circle */
[data-testid="stChatInput"] button {
    background-color: var(--accent) !important;
    color: white !important;
    border-radius: 50% !important;
    border: none !important;
    padding: 4px !important;
    transition: all 0.2s !important;
}
[data-testid="stChatInput"] button:hover {
    background-color: var(--accent-hover) !important;
    transform: scale(1.05) !important;
}

/* Sticky Bottom Bar Match Page Background */
div[data-testid="stBottom"] {
    background-color: var(--bg) !important;
}
div[data-testid="stBottomBlockContainer"] {
    background-color: var(--bg) !important;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 6px !important;
    height: 6px !important;
}
::-webkit-scrollbar-track {
    background: transparent !important;
}
::-webkit-scrollbar-thumb {
    background: var(--border) !important;
    border-radius: 4px !important;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted) !important;
}

/* Force all columns inside the sidebar to have ZERO padding/margin, packing items vertically */
[data-testid="stSidebar"] [data-testid="column"] {
    padding: 0 !important;
    margin: 0 !important;
}

/* Global Sidebar Button overrides: Removes bulky boxes, borders and gray backgrounds */
[data-testid="stSidebar"] .stButton button,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"],
.stSidebar .stButton button,
.stSidebar .stButton [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 3px 0px !important; /* Zero out left padding, minimal vertical padding */
    border-radius: 0px !important;
    font-size: 14px !important;
    width: 100% !important;
    height: auto !important;
    display: flex !important;
    align-items: center !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    transition: color 0.15s ease !important;
    margin: 0 !important;
}
[data-testid="stSidebar"] .stButton button:hover,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:hover,
[data-testid="stSidebar"] .stButton button:focus,
[data-testid="stSidebar"] .stButton button:active,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:focus,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:active,
.stSidebar .stButton button:hover,
.stSidebar .stButton [data-testid="stBaseButton-secondary"]:hover {
    background-color: transparent !important; /* Absolutely transparent on hover/focus */
    color: #ffffff !important; /* Plain white text */
    border: none !important;
    box-shadow: none !important;
}

/* Sidebar Brand container styling */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-brand-container) [data-testid="stHorizontalBlock"] {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 10px 12px 6px 12px !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-brand-container) [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: auto !important;
    min-width: unset !important;
    flex: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
.st-key-sidebar_theme_toggle button,
.st-key-sidebar_theme_toggle [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    width: 38px !important;
    height: 38px !important;
    min-width: 38px !important;
    min-height: 38px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 16px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
}
.st-key-sidebar_theme_toggle button:hover,
.st-key-sidebar_theme_toggle [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}

/* High-specificity selector for New Chat button to keep its beautiful capsule shape */
.st-key-new_chat_btn {
    width: 100% !important;
    padding: 0 12px !important;
    box-sizing: border-box !important;
}
.st-key-new_chat_btn button,
.st-key-new_chat_btn [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 24px !important;
    padding: 10px 16px !important;
    color: var(--text) !important;
    font-weight: 500 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    width: 100% !important;
}
.st-key-new_chat_btn button:hover,
.st-key-new_chat_btn [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}

/* Mock rows like Settings */
.sidebar-menu-row {
    padding: 8px 16px !important;
    font-size: 14.5px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    cursor: default !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    border-radius: 8px !important;
    margin: 4px 8px !important;
    transition: background-color 0.2s !important;
}
.sidebar-menu-row:hover {
    background-color: var(--hover) !important;
}

/* Make sure the empty class markers are completely hidden and take no layout space */
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .history-logs-container),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .history-item-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .active-chat-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .profile-trigger-card) {
    visibility: hidden !important;
    position: absolute !important;
    width: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Pack history rows — zero gap */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-logs-container) {
    gap: 0px !important;
}
[data-testid="stSidebar"] div[data-testid="element-container"]:has(.history-item-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(.active-chat-row) {
    margin: 0 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) {
    margin: 0px 8px !important;
    padding: 0 !important;
    gap: 0px !important;
}
/* Collapse inner gaps inside each chat row */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) > div,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) > div {
    gap: 0px !important;
    margin: 0 !important;
    padding: 0 !important;
}
/* Remove any Streamlit default element spacing between rows */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-logs-container) [data-testid="element-container"] {
    margin: 0 !important;
    padding: 0 !important;
}
/* Columns inside each row: tight, centered */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stHorizontalBlock"],
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] {
    gap: 0px !important;
    align-items: center !important;
}
/* Dots column: fixed narrow width */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child {
    flex: 0 0 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
    overflow: visible !important;
    padding: 0 !important;
}
/* Dots popover button compact & single-line */
[data-testid="stSidebar"] div[class*="stPopover"],
[data-testid="stSidebar"] div[class*="stPopover"] > div,
[data-testid="stSidebar"] [data-testid="stPopover"],
[data-testid="stSidebar"] [data-testid="stPopover"] > div,
[data-testid="stSidebar"] [data-testid="column"]:last-child button,
.stSidebar div[class*="stPopover"],
.stSidebar [data-testid="stPopover"],
div[class*="stPopover"],
[data-testid="stPopover"] {
    width: 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
}
[data-testid="stSidebar"] div[class*="stPopover"] button,
[data-testid="stSidebar"] [data-testid="stPopover"] button,
[data-testid="stSidebar"] [data-testid="column"]:last-child button,
.stSidebar div[class*="stPopover"] button,
.stSidebar [data-testid="stPopover"] button,
div[class*="stPopover"] button,
[data-testid="stPopover"] button {
    width: 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
    padding: 3px 2px !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    line-height: 1 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
[data-testid="stSidebar"] div[class*="stPopover"] button svg,
[data-testid="stSidebar"] div[class*="stPopover"] button div[data-testid="stIcon"],
[data-testid="stSidebar"] div[class*="stPopover"] button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="stPopover"] button svg,
[data-testid="stSidebar"] [data-testid="stPopover"] button div[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="stPopover"] button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button svg,
[data-testid="stSidebar"] [data-testid="column"]:last-child button div[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button::after,
[data-testid="stSidebar"] [data-testid="column"]:last-child button::before,
.stSidebar div[class*="stPopover"] button svg,
.stSidebar div[class*="stPopover"] button [data-testid="stIcon"],
.stSidebar div[class*="stPopover"] button [class*="Icon"],
div[class*="stPopover"] button svg,
div[class*="stPopover"] button [data-testid="stIcon"],
div[class*="stPopover"] button [class*="Icon"],
[data-testid="stPopover"] button svg,
[data-testid="stPopover"] button [data-testid="stIcon"],
[data-testid="stPopover"] button [class*="Icon"],
[data-testid="stPopover"] button::after,
[data-testid="stPopover"] button::before {
    display: none !important;
    content: none !important;
}

/* Active chat row container styled as a beautiful capsule pill (specific to avoid main sidebar) */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) {
    background-color: var(--hover) !important; /* Lighter grey background capsule */
    border-radius: 8px !important;
    margin: 0px 12px !important; /* Same margins for perfect alignment */
    padding: 0px 4px 0px 0px !important; /* Only right padding for inline actions */
    gap: 0px !important;
}

/* Active chat row column alignment overrides */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] {
    align-items: center !important;
    justify-content: space-between !important;
    gap: 0px !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="column"] {
    padding: 0 !important;
    margin: 0 !important;
    flex: none !important;
    width: auto !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="column"]:first-child {
    flex-grow: 1 !important;
    min-width: 0 !important;
}

/* Active chat action icons layout */
.active-chat-actions {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    gap: 8px !important;
    color: var(--text-muted) !important;
    padding-left: 8px !important;
    padding-right: 8px !important;
    height: 32px !important;
}
.active-chat-actions .action-btn {
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: var(--text-muted) !important;
    transition: color 0.15s ease !important;
}
.active-chat-actions .action-btn:hover {
    color: var(--text) !important;
}

/* Style all history buttons as transparent plain-text links */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stBaseButton-secondary"],
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 3px 8px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    width: 100% !important;
    height: auto !important;
    display: flex !important;
    align-items: center !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    transition: color 0.15s ease !important;
    margin: 0 !important;
}

[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stBaseButton-secondary"]:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"]:hover {
    background-color: transparent !important;
    color: #ffffff !important;
    border: none !important;
}

/* Active chat log highlights with pure white text and bold weight */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* Prevent text wrapping and enforce strict single-line ellipsis truncation on history log buttons and all nested children */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button *,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button * {
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    max-width: 100% !important;
    min-width: 0 !important;
}

/* Sidebar Logout Pill Capsule button */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton {
    width: 100% !important;
    padding: 0 12px !important;
    box-sizing: border-box !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton > button {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 24px !important;
    padding: 10px 16px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton > button:hover {
    background-color: var(--hover) !important;
}

/* Starter Prompts Container */
.starter-container {
    max-width: 768px;
    margin: 20px auto 0 auto;
}
.starter-container .stButton > button {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 16px !important;
    text-align: left !important;
    font-size: 14px !important;
    white-space: pre-line !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
    min-height: 84px !important;
    display: flex !important;
    align-items: flex-start !important;
    justify-content: flex-start !important;
    line-height: 1.4 !important;
}
.starter-container .stButton > button:hover {
    background-color: var(--hover) !important;
    border-color: var(--accent) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
}

/* Custom Cards */
.brand-title {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, var(--accent), #56e39f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Form Styling overrides: Style the form as the login card container */
[data-testid="stForm"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    padding: 32px !important;
    box-shadow: 0 10px 30px var(--shadow) !important;
    margin-top: 40px !important;
    margin-bottom: 24px !important;
}

/* Selectbox and Input overrides */
div[data-baseweb="select"] > div {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}
div[data-baseweb="select"] svg {
    fill: var(--text) !important;
}
.stTextInput input, .stTextArea textarea {
    background-color: #1b1b1c !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.25) !important;
    outline: none !important;
}

/* Hide form instruction overlays */
[data-testid="InputInstructions"] {
    display: none !important;
}

/* Right-align copy button for user messages */
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.user-copy) {
    display: flex !important;
    justify-content: flex-end !important;
}

/* Message copy actions container wrapped style override */
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button,
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button[kind="secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 12.5px !important;
    color: var(--text-muted) !important;
    padding: 4px 10px !important;
    height: auto !important;
    min-height: unset !important;
    width: auto !important;
    border-radius: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
}
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button:hover,
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button[kind="secondary"]:hover {
    color: var(--text) !important;
    background-color: var(--hover) !important;
    border: none !important;
}
/* Style stExpander inside the export container to be exceptionally sleek */
div[data-testid="stVerticalBlock"]:has(.export-container) [data-testid="stExpander"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
}
div[data-testid="stVerticalBlock"]:has(.export-container) [data-testid="stExpander"] summary {
    font-size: 13.5px !important;
    font-weight: 500 !important;
    padding: 6px 12px !important;
}

/* Message timestamp */
.msg-time {
    font-size: 11.5px !important;
    color: var(--text-muted) !important;
    opacity: 0.65 !important;
    padding: 4px 0 !important;
}

/* Copy button next to timestamp */
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button,
[data-testid="stMainBlockContainer"] [class*="st-key-copy_live_"] button {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 14px !important;
    padding: 2px 6px !important;
    border-radius: 6px !important;
    height: auto !important;
    min-height: unset !important;
    width: auto !important;
    transition: background-color 0.15s, color 0.15s !important;
}
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button:hover,
[data-testid="stMainBlockContainer"] [class*="st-key-copy_live_"] button:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Bottom disclaimer — fixed below the chat input */
.chat-footer-text {
    position: fixed !important;
    bottom: 6px !important;
    left: 260px !important;
    right: 0 !important;
    text-align: center !important;
    font-size: 11.5px !important;
    color: var(--text-muted) !important;
    z-index: 996 !important;
    pointer-events: none !important;
    background: transparent !important;
}

/* Code Highlights and pre-wraps */
code, pre {
    background-color: var(--code-bg) !important;
    color: var(--code-text) !important;
    border-radius: 8px !important;
}
pre {
    padding: 16px !important;
    border: 1px solid var(--border) !important;
}
.token-badge {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12.5px;
    color: var(--text-muted);
    display: inline-block;
}

/* User Profile footer card in sidebar */
.user-profile-card {
    background-color: transparent;
    border: none;
    padding: 10px;
    margin-top: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.user-avatar {
    background: linear-gradient(135deg, #7c83fd, #a78bfa) !important;
    border-radius: 50% !important;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: white;
    font-size: 14px;
    min-width: 38px;
    min-height: 38px;
}

/* Sticky top bar details */
.sticky-top-bar {
    text-align: center;
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
    background-color: var(--bg);
    margin-bottom: 16px;
    font-size: 13px;
    color: var(--text-muted);
}

[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 260px !important;
    background-color: var(--sidebar) !important;
    border-top: 1px solid var(--border) !important;
    padding: 4px 14px 16px 14px !important;
    z-index: 10000 !important;
    box-shadow: 0 -6px 20px rgba(0,0,0,0.15) !important;
    gap: 0px !important;
}
section[data-testid="stSidebar"][data-collapsed="true"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) {
    display: none !important;
    visibility: hidden !important;
}

/* Push scrollable area above fixed footer */
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding-bottom: 160px !important;
}

/* Floating Profile Popup Menu styling */
.profile-popup-menu {
    position: absolute !important;
    bottom: 64px !important;
    left: 12px !important;
    right: 12px !important;
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 10px !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35) !important;
    z-index: 1000 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
}

/* Style the buttons inside the profile popup menu as list rows */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton button,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 10px 14px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    transition: background-color 0.15s ease !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton button:hover,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border: none !important;
}

/* ··· popover trigger button */
[data-testid="stSidebar"] [data-testid="stPopover"] button,
[data-testid="stSidebar"] [data-testid="stPopover"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 16px !important;
    letter-spacing: 2px !important;
    padding: 2px 6px !important;
    border-radius: 6px !important;
    width: auto !important;
    height: auto !important;
    min-height: unset !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background-color 0.15s, color 0.15s !important;
}
[data-testid="stSidebar"] [data-testid="stPopover"] button:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Floating popover panel */
[data-testid="stPopoverBody"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 6px !important;
    box-shadow: 0 8px 30px var(--shadow) !important;
    min-width: 160px !important;
}

/* Delete button inside popover */
[class*="st-key-del_"] button,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #e74c3c !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    transition: background-color 0.15s !important;
}
[class*="st-key-del_"] button:hover,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: rgba(231,76,60,0.15) !important;
    border: none !important;
}

/* Profile card row (bottom of sidebar) */
.profile-card-row {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 8px 0px !important;
    cursor: default !important;
    margin-bottom: 6px !important;
}

/* Sidebar Logout Button Styling matching Image 1 exactly */
.st-key-menu_logout,
.st-key-menu_logout > div {
    width: 100% !important;
}
.st-key-menu_logout button,
.st-key-menu_logout [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 10px 16px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 10px !important;
    width: 100% !important;
    height: auto !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
}
.st-key-menu_logout button:hover,
.st-key-menu_logout [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: #ffffff !important;
    border: 1px solid var(--border) !important;
}

.profile-card-text {
    flex: 1 !important;
    overflow: hidden !important;
    min-width: 0 !important;
}
.profile-card-name {
    font-weight: 600 !important;
    font-size: 13.5px !important;
    color: var(--text) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
.profile-card-plan {
    font-size: 11px !important;
    color: var(--text-muted) !important;
    margin-top: 1px !important;
}

/* Grid icon button (⊞) */
.st-key-profile_trigger button,
.st-key-profile_trigger [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 18px !important;
    padding: 4px 8px !important;
    border-radius: 6px !important;
    width: auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background-color 0.15s ease !important;
}
.st-key-profile_trigger button:hover,
.st-key-profile_trigger [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Profile popup card */
.profile-popup-card {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 8px 10px !important;
    border-radius: 8px !important;
}
.popup-info { flex: 1; overflow: hidden; min-width: 0; }
.popup-name {
    font-weight: 600 !important;
    font-size: 13.5px !important;
    color: var(--text) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
.popup-plan { font-size: 11px !important; color: var(--text-muted) !important; margin-top: 1px !important; }

/* Search chats button styling */
.st-key-search_chats_btn button,
.st-key-search_chats_btn [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 6px 12px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 400 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: background-color 0.15s ease, color 0.15s ease !important;
}
.st-key-search_chats_btn button:hover,
.st-key-search_chats_btn [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Logout button inside popup */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-card) ~ div .st-key-menu_logout button,
.st-key-menu_logout button,
.st-key-menu_logout [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
}
.st-key-menu_logout button:hover,
.st-key-menu_logout [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border: none !important;
}

/* All sidebar buttons: transparent background, no border, no box-shadow */
[data-testid="stSidebar"] button,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] button:hover,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border: none !important;
}

/* Delete button inside popover: render in red text */
[class*="st-key-del_"] button,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"] {
    color: #ff4b4b !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
[class*="st-key-del_"] button:hover,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: rgba(255, 75, 75, 0.1) !important;
    color: #ff4b4b !important;
    border: none !important;
}

/* Sidebar footer container flex columns */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="element-container"] {
    margin: 0 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 8px !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: auto !important;
    flex: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
/* Username column should expand to take remaining space */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"]:nth-child(2) {
    flex: 1 !important;
    min-width: 0 !important;
}
/* Popover column on the right */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"]:nth-child(3) {
    flex: 0 0 auto !important;
}

/* Hide Streamlit Popover Chevron icons (targets material expand_more and expand_less icons) */
[data-testid="stSidebar"] [data-testid="stPopover"] button div[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="stPopover"] button span[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="stPopover"] button [class*="eucf0wj1"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button div[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button span[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button [class*="eucf0wj1"],
[class*="eucf0wj1"] {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    visibility: hidden !important;
    opacity: 0 !important;
}
</style>
"""

LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --bg: #ffffff;
    --sidebar: #f9f9f9;
    --surface: #ffffff;
    --border: #e5e5e5;
    --text: #0d0d0d;
    --text-muted: #676767;
    --accent: #10a37f;
    --accent-hover: #1a7f64;
    --hover: #ececec;
    --code-bg: #f6f8fa;
    --code-text: #24292e;
    --shadow: rgba(0, 0, 0, 0.05);
    --user-bubble: #f4f4f4;
    --text2: #676767;
}

/* Global overrides */
body, .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}

[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] *,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] li,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] span,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] strong,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] em,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h1,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h3,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h4,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h5,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] h6 {
    color: var(--text) !important;
}

[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] code,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] pre {
    color: var(--code-text) !important;
    background-color: var(--code-bg) !important;
}

label,
.stTextInput label,
.stTextArea label,
[data-testid="stWidgetLabel"] p {
    color: var(--text) !important;
}

/* Hide default Streamlit headers and footers */
[data-testid="stHeader"] {
    background-color: transparent !important;
    border-bottom: none !important;
}
footer {
    display: none !important;
    visibility: hidden !important;
}
#MainMenu {
    visibility: hidden !important;
}

/* Hide Default Sidebar Multi-page Navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Hide default Streamlit sidebar header globally to eliminate empty space at the top of the sidebar */
[data-testid="stSidebarHeader"],
div[class*="stSidebarHeader"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Sidebar Custom Styling */
[data-testid="stSidebar"] {
    background-color: var(--sidebar) !important;
    border-right: 1px solid var(--border) !important;
    width: 260px !important;
}
/* Eliminate the massive Streamlit default padding at the top of the sidebar and hide horizontal overflow */
[data-testid="stSidebarUserContent"] {
    padding-top: 6px !important;
    padding-bottom: 10px !important;
    overflow-x: hidden !important;
}
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    overflow-x: hidden !important;
}
@media (min-width: 768px) {
    /* Lock the sidebar permanently as a fixed panel on desktops, overriding collapse states */
    [data-testid="stSidebar"],
    section[data-testid="stSidebar"][data-collapsed="true"] {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        bottom: 0 !important;
        width: 260px !important;
        min-width: 260px !important;
        max-width: 260px !important;
        transform: translate3d(0, 0, 0) !important;
        transition: none !important;
        display: block !important;
        visibility: visible !important;
        z-index: 1000 !important;
    }
    /* Force the inner containers inside the sidebar to remain visible and fully open */
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] [data-testid="stSidebarUserContent"],
    section[data-testid="stSidebar"][data-collapsed="true"] > div,
    section[data-testid="stSidebar"][data-collapsed="true"] [data-testid="stSidebarUserContent"] {
        width: 260px !important;
        min-width: 260px !important;
        max-width: 260px !important;
        visibility: visible !important;
        display: block !important;
        opacity: 1 !important;
        transform: none !important;
    }
    /* Push main chat container to the right to make space for the fixed sidebar */
    .stMain, [data-testid="stMainBlockContainer"] {
        margin-left: 260px !important;
        width: calc(100% - 260px) !important;
        max-width: 100% !important;
    }
    /* Hide Streamlit collapse, expand and sidebar header containers to remove empty top space completely on desktops */
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapseButton"],
    button[data-testid="sidebar-collapse-button"],
    div[class*="collapsedControl"],
    [data-testid="stSidebarHeader"],
    div[class*="stSidebarHeader"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
}

[data-testid="stSidebar"] > div {
    background-color: var(--sidebar) !important;
}
[data-testid="stSidebar"] * {
    color: var(--text) !important;
}

/* Fixed Header Bar at the top of the main viewport */
.fixed-top-header {
    position: fixed !important;
    top: 0 !important;
    left: 260px !important;
    right: 0 !important;
    height: 56px !important;
    background-color: var(--bg) !important;
    border-bottom: 1px solid var(--border) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    padding: 0 24px !important;
    z-index: 998 !important;
}
@media (max-width: 768px) {
    .fixed-top-header {
        left: 0 !important;
    }
}

/* Floating Theme Toggle buttons - Side-by-side and Compact at top right corner */
.theme-toggle-fixed {
    position: fixed !important;
    top: 12px !important;
    right: 24px !important;
    z-index: 9999 !important;
    display: flex !important;
    flex-direction: row !important;
    gap: 8px !important;
    width: auto !important;
}
.theme-toggle-fixed [data-testid="column"] {
    width: auto !important;
    flex: none !important;
}
.theme-toggle-fixed .stButton > button {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
    min-width: 32px !important;
    min-height: 32px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 14px !important;
    box-shadow: 0 2px 8px var(--shadow) !important;
}
.theme-toggle-fixed .stButton > button:hover {
    background-color: var(--hover) !important;
    border-color: var(--accent) !important;
}

/* Push main chat container down and center content */
[data-testid="stMainBlockContainer"] {
    padding-top: 56px !important;
    padding-bottom: 30px !important;
    padding-left: 10% !important;
    padding-right: 10% !important;
    margin-top: 0 !important;
    max-width: 800px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
@media (max-width: 1200px) {
    [data-testid="stMainBlockContainer"] {
        padding-left: 5% !important;
        padding-right: 5% !important;
    }
}
@media (min-width: 768px) {
    [data-testid="stHeader"] {
        display: none !important;
    }
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="primary"] {
    background-color: var(--accent) !important;
    color: white !important;
    border: 1px solid var(--accent) !important;
    border-radius: 20px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 8px 16px !important;
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="secondary"] {
    background-color: var(--surface) !important;
    color: var(--text-muted) !important;
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 8px 16px !important;
}
[data-testid="stMainBlockContainer"] .stButton > button[kind="secondary"]:hover {
    color: var(--text) !important;
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}


/* Centering Chat Elements to 768px */
[data-testid="stChatMessage"] {
    max-width: 768px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    background-color: transparent !important;
    border: none !important;
    padding: 1rem 0 !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
}
[data-testid="stChatMessage"] [data-testid="stAvatar"] {
    border-radius: 50% !important;
    border: 1px solid var(--border) !important;
    background-color: var(--hover) !important;
}

/* Custom Message Layouts (ChatGPT look) */
.chat-user-message {
    background-color: var(--user-bubble) !important;
    color: var(--text) !important;
    border-radius: 20px !important;
    padding: 10px 18px !important;
    display: inline-block !important;
    max-width: 85% !important;
    margin-bottom: 4px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    border: 1px solid var(--border) !important;
}
.chat-assistant-message {
    color: var(--text) !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
}

/* Custom Chat Input styling - Exhaustive overrides */
[data-testid="stChatInput"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 26px !important;
    box-shadow: 0 4px 20px var(--shadow) !important;
    max-width: 100% !important;
    margin: 0 auto 10px auto !important;
    padding: 4px 12px !important;
}
/* Force all inner wrappers to be completely transparent to eliminate the dark rectangle */
[data-testid="stChatInput"] div,
[data-testid="stChatInput"] textarea {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--text) !important;
    font-size: 15px !important;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    outline: none !important;
}
/* Send button inside input styled as a circle */
[data-testid="stChatInput"] button {
    background-color: var(--accent) !important;
    color: white !important;
    border-radius: 50% !important;
    border: none !important;
    padding: 4px !important;
    transition: all 0.2s !important;
}
[data-testid="stChatInput"] button:hover {
    background-color: var(--accent-hover) !important;
    transform: scale(1.05) !important;
}

/* Sticky Bottom Bar Match Page Background */
div[data-testid="stBottom"] {
    background-color: var(--bg) !important;
}
div[data-testid="stBottomBlockContainer"] {
    background-color: var(--bg) !important;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 6px !important;
    height: 6px !important;
}
::-webkit-scrollbar-track {
    background: transparent !important;
}
::-webkit-scrollbar-thumb {
    background: var(--border) !important;
    border-radius: 4px !important;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted) !important;
}

/* Force all columns inside the sidebar to have ZERO padding/margin, packing items vertically */
[data-testid="stSidebar"] [data-testid="column"] {
    padding: 0 !important;
    margin: 0 !important;
}

/* Global Sidebar Button overrides: Removes bulky boxes, borders and gray backgrounds */
[data-testid="stSidebar"] .stButton button,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"],
.stSidebar .stButton button,
.stSidebar .stButton [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 3px 0px !important; /* Zero out left padding, minimal vertical padding */
    border-radius: 0px !important;
    font-size: 14px !important;
    width: 100% !important;
    height: auto !important;
    display: flex !important;
    align-items: center !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    transition: color 0.15s ease !important;
    margin: 0 !important;
}
[data-testid="stSidebar"] .stButton button:hover,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:hover,
[data-testid="stSidebar"] .stButton button:focus,
[data-testid="stSidebar"] .stButton button:active,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:focus,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:active,
.stSidebar .stButton button:hover,
.stSidebar .stButton [data-testid="stBaseButton-secondary"]:hover {
    background-color: transparent !important; /* Absolutely transparent on hover/focus */
    color: var(--text) !important; /* High contrast theme text color */
    border: none !important;
    box-shadow: none !important;
}

/* Sidebar Brand container styling */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-brand-container) [data-testid="stHorizontalBlock"] {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 10px 12px 6px 12px !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-brand-container) [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: auto !important;
    min-width: unset !important;
    flex: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
.st-key-sidebar_theme_toggle button,
.st-key-sidebar_theme_toggle [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    width: 38px !important;
    height: 38px !important;
    min-width: 38px !important;
    min-height: 38px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 16px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
}
.st-key-sidebar_theme_toggle button:hover,
.st-key-sidebar_theme_toggle [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}

/* High-specificity selector for New Chat button to keep its beautiful capsule shape */
.st-key-new_chat_btn {
    width: 100% !important;
    padding: 0 12px !important;
    box-sizing: border-box !important;
}
.st-key-new_chat_btn button,
.st-key-new_chat_btn [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 24px !important;
    padding: 10px 16px !important;
    color: var(--text) !important;
    font-weight: 500 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    width: 100% !important;
}
.st-key-new_chat_btn button:hover,
.st-key-new_chat_btn [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border-color: var(--border) !important;
}

/* Mock rows like Settings */
.sidebar-menu-row {
    padding: 8px 16px !important;
    font-size: 14.5px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    cursor: default !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    border-radius: 8px !important;
    margin: 4px 8px !important;
    transition: background-color 0.2s !important;
}
.sidebar-menu-row:hover {
    background-color: var(--hover) !important;
}

/* Make sure the empty class markers are completely hidden and take no layout space */
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .history-logs-container),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .history-item-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .active-chat-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .profile-trigger-card) {
    visibility: hidden !important;
    position: absolute !important;
    width: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Pack history rows — zero gap */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-logs-container) {
    gap: 0px !important;
}
[data-testid="stSidebar"] div[data-testid="element-container"]:has(.history-item-row),
[data-testid="stSidebar"] div[data-testid="element-container"]:has(.active-chat-row) {
    margin: 0 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) {
    margin: 0px 8px !important;
    padding: 0 !important;
    gap: 0px !important;
}
/* Collapse inner gaps inside each chat row */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) > div,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) > div {
    gap: 0px !important;
    margin: 0 !important;
    padding: 0 !important;
}
/* Remove any Streamlit default element spacing between rows */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-logs-container) [data-testid="element-container"] {
    margin: 0 !important;
    padding: 0 !important;
}
/* Columns inside each row: tight, centered */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stHorizontalBlock"],
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] {
    gap: 0px !important;
    align-items: center !important;
}
/* Dots column: fixed narrow width */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child {
    flex: 0 0 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
    overflow: visible !important;
    padding: 0 !important;
}
/* Dots popover button compact & single-line */
[data-testid="stSidebar"] div[class*="stPopover"],
[data-testid="stSidebar"] div[class*="stPopover"] > div,
[data-testid="stSidebar"] [data-testid="stPopover"],
[data-testid="stSidebar"] [data-testid="stPopover"] > div,
[data-testid="stSidebar"] [data-testid="column"]:last-child button,
.stSidebar div[class*="stPopover"],
.stSidebar [data-testid="stPopover"],
div[class*="stPopover"],
[data-testid="stPopover"] {
    width: 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
}
[data-testid="stSidebar"] div[class*="stPopover"] button,
[data-testid="stSidebar"] [data-testid="stPopover"] button,
[data-testid="stSidebar"] [data-testid="column"]:last-child button,
.stSidebar div[class*="stPopover"] button,
.stSidebar [data-testid="stPopover"] button,
div[class*="stPopover"] button,
[data-testid="stPopover"] button {
    width: 28px !important;
    min-width: 28px !important;
    max-width: 28px !important;
    padding: 3px 2px !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    line-height: 1 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
[data-testid="stSidebar"] div[class*="stPopover"] button svg,
[data-testid="stSidebar"] div[class*="stPopover"] button div[data-testid="stIcon"],
[data-testid="stSidebar"] div[class*="stPopover"] button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="stPopover"] button svg,
[data-testid="stSidebar"] [data-testid="stPopover"] button div[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="stPopover"] button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button svg,
[data-testid="stSidebar"] [data-testid="column"]:last-child button div[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button span[data-testid="stIcon"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button::after,
[data-testid="stSidebar"] [data-testid="column"]:last-child button::before,
.stSidebar div[class*="stPopover"] button svg,
.stSidebar div[class*="stPopover"] button [data-testid="stIcon"],
.stSidebar div[class*="stPopover"] button [class*="Icon"],
div[class*="stPopover"] button svg,
div[class*="stPopover"] button [data-testid="stIcon"],
div[class*="stPopover"] button [class*="Icon"],
[data-testid="stPopover"] button svg,
[data-testid="stPopover"] button [data-testid="stIcon"],
[data-testid="stPopover"] button [class*="Icon"],
[data-testid="stPopover"] button::after,
[data-testid="stPopover"] button::before {
    display: none !important;
    content: none !important;
}

/* Active chat row container styled as a beautiful capsule pill (specific to avoid main sidebar) */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) {
    background-color: var(--hover) !important; /* Lighter grey background capsule */
    border-radius: 8px !important;
    margin: 0px 12px !important; /* Same margins for perfect alignment */
    padding: 0px 4px 0px 0px !important; /* Only right padding for inline actions */
    gap: 0px !important;
}

/* Active chat row column alignment overrides */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stHorizontalBlock"] {
    align-items: center !important;
    justify-content: space-between !important;
    gap: 0px !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="column"] {
    padding: 0 !important;
    margin: 0 !important;
    flex: none !important;
    width: auto !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="column"]:first-child {
    flex-grow: 1 !important;
    min-width: 0 !important;
}

/* Active chat action icons layout */
.active-chat-actions {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    gap: 8px !important;
    color: var(--text-muted) !important;
    padding-left: 8px !important;
    padding-right: 8px !important;
    height: 32px !important;
}
.active-chat-actions .action-btn {
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: var(--text-muted) !important;
    transition: color 0.15s ease !important;
}
.active-chat-actions .action-btn:hover {
    color: var(--text) !important;
}

/* Style all history buttons as transparent plain-text links */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stBaseButton-secondary"],
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 3px 8px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    width: 100% !important;
    height: auto !important;
    display: flex !important;
    align-items: center !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    transition: color 0.15s ease !important;
    margin: 0 !important;
}

[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) [data-testid="stBaseButton-secondary"]:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"]:hover {
    background-color: transparent !important;
    color: var(--text) !important;
    border: none !important;
}

/* Active chat log highlights with high-contrast text and bold weight */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    color: var(--text) !important;
    font-weight: 600 !important;
}

/* Prevent text wrapping and enforce strict single-line ellipsis truncation on history log buttons and all nested children */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button *,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button * {
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    max-width: 100% !important;
    min-width: 0 !important;
}

/* Sidebar Logout Pill Capsule button */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton {
    width: 100% !important;
    padding: 0 12px !important;
    box-sizing: border-box !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton > button {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 24px !important;
    padding: 10px 16px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-logout-btn) .stButton > button:hover {
    background-color: var(--hover) !important;
}

/* Starter Prompts Container */
.starter-container {
    max-width: 768px;
    margin: 20px auto 0 auto;
}
.starter-container .stButton > button {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 16px !important;
    text-align: left !important;
    font-size: 14px !important;
    white-space: pre-line !important;
    box-shadow: 0 2px 10px var(--shadow) !important;
    transition: all 0.2s ease !important;
    min-height: 84px !important;
    display: flex !important;
    align-items: flex-start !important;
    justify-content: flex-start !important;
    line-height: 1.4 !important;
}
.starter-container .stButton > button:hover {
    background-color: var(--hover) !important;
    border-color: var(--accent) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
}

/* Custom Cards */
.brand-title {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, var(--accent), #0e8568);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Form Styling overrides: Style the form as the login card container */
[data-testid="stForm"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    padding: 32px !important;
    box-shadow: 0 10px 30px var(--shadow) !important;
    margin-top: 40px !important;
    margin-bottom: 24px !important;
}

/* Selectbox and Input overrides */
div[data-baseweb="select"] > div {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}
div[data-baseweb="select"] svg {
    fill: var(--text) !important;
}
.stTextInput input, .stTextArea textarea {
    background-color: #f9f9f9 !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.2) !important;
    outline: none !important;
}

/* Hide form instruction overlays */
[data-testid="InputInstructions"] {
    display: none !important;
}

/* Right-align copy button for user messages */
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.user-copy) {
    display: flex !important;
    justify-content: flex-end !important;
}

/* Message copy actions container wrapped style override */
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button,
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button[kind="secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 12.5px !important;
    color: var(--text-muted) !important;
    padding: 4px 10px !important;
    height: auto !important;
    min-height: unset !important;
    width: auto !important;
    border-radius: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
}
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button:hover,
[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlock"]:has(.message-copy-container) .stButton > button[kind="secondary"]:hover {
    color: var(--text) !important;
    background-color: var(--hover) !important;
    border: none !important;
}
/* Style stExpander inside the export container to be exceptionally sleek */
div[data-testid="stVerticalBlock"]:has(.export-container) [data-testid="stExpander"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
}
div[data-testid="stVerticalBlock"]:has(.export-container) [data-testid="stExpander"] summary {
    font-size: 13.5px !important;
    font-weight: 500 !important;
    padding: 6px 12px !important;
}

/* Message timestamp */
.msg-time {
    font-size: 11.5px !important;
    color: var(--text-muted) !important;
    opacity: 0.65 !important;
    padding: 4px 0 !important;
}

/* Copy button next to timestamp */
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button,
[data-testid="stMainBlockContainer"] [class*="st-key-copy_live_"] button {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 14px !important;
    padding: 2px 6px !important;
    border-radius: 6px !important;
    height: auto !important;
    min-height: unset !important;
    width: auto !important;
    transition: background-color 0.15s, color 0.15s !important;
}
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button:hover,
[data-testid="stMainBlockContainer"] [class*="st-key-copy_live_"] button:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Bottom disclaimer — fixed below the chat input */
.chat-footer-text {
    position: fixed !important;
    bottom: 6px !important;
    left: 260px !important;
    right: 0 !important;
    text-align: center !important;
    font-size: 11.5px !important;
    color: var(--text-muted) !important;
    z-index: 996 !important;
    pointer-events: none !important;
    background: transparent !important;
}

/* Code Highlights and pre-wraps */
code, pre {
    background-color: var(--code-bg) !important;
    color: var(--code-text) !important;
    border-radius: 8px !important;
}
pre {
    padding: 16px !important;
    border: 1px solid var(--border) !important;
}
.token-badge {
    background: var(--hover);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12.5px;
    color: var(--text-muted);
    display: inline-block;
}

/* User Profile footer card in sidebar */
.user-profile-card {
    background-color: transparent;
    border: none;
    padding: 10px;
    margin-top: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.user-avatar {
    background: linear-gradient(135deg, #7c83fd, #a78bfa) !important;
    border-radius: 50% !important;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: white;
    font-size: 14px;
    min-width: 38px;
    min-height: 38px;
}

/* Sticky top bar details */
.sticky-top-bar {
    text-align: center;
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
    background-color: var(--bg);
    margin-bottom: 16px;
    font-size: 13px;
    color: var(--text-muted);
}

[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 260px !important;
    background-color: var(--sidebar) !important;
    border-top: 1px solid var(--border) !important;
    padding: 4px 14px 16px 14px !important;
    z-index: 10000 !important;
    box-shadow: 0 -6px 20px rgba(0,0,0,0.15) !important;
    gap: 0px !important;
}
section[data-testid="stSidebar"][data-collapsed="true"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) {
    display: none !important;
    visibility: hidden !important;
}

/* Push scrollable area above fixed footer */
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding-bottom: 160px !important;
}

/* Floating Profile Popup Menu styling */
.profile-popup-menu {
    position: absolute !important;
    bottom: 64px !important;
    left: 12px !important;
    right: 12px !important;
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 10px !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08) !important;
    z-index: 1000 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
}

/* Style the buttons inside the profile popup menu as list rows */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton button,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 10px 14px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    transition: background-color 0.15s ease !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton button:hover,
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.profile-popup-menu) .stButton [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border: none !important;
}

/* Dots (···) button per chat row */
[data-testid="stSidebar"] [class*="st-key-dots_"] button,
[data-testid="stSidebar"] [class*="st-key-dots_"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 15px !important;
    letter-spacing: 1px !important;
    padding: 2px 6px !important;
    border-radius: 6px !important;
    width: auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background-color 0.15s, color 0.15s !important;
}
[data-testid="stSidebar"] [class*="st-key-dots_"] button:hover,
[data-testid="stSidebar"] [class*="st-key-dots_"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Floating popover panel */
[data-testid="stPopoverBody"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 6px !important;
    box-shadow: 0 8px 30px var(--shadow) !important;
    min-width: 160px !important;
}

/* Chat context menu popup (Delete panel) */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.chat-context-menu) {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 4px 8px !important;
    margin: 2px 12px 6px 12px !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
}
[data-testid="stSidebar"] div[data-testid="element-container"]:has(> div[data-testid="stMarkdownContainer"] > .chat-context-menu) {
    visibility: hidden !important;
    position: absolute !important;
    width: 0 !important;
    height: 0 !important;
}
[data-testid="stSidebar"] [class*="st-key-del_"] button,
[data-testid="stSidebar"] [class*="st-key-del_"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #e74c3c !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 8px 10px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: background-color 0.15s !important;
}
[data-testid="stSidebar"] [class*="st-key-del_"] button:hover,
[data-testid="stSidebar"] [class*="st-key-del_"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: rgba(231,76,60,0.12) !important;
    border: none !important;
}

/* Profile card row (bottom of sidebar) */
.profile-card-row {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 8px 0px !important;
    cursor: default !important;
    margin-bottom: 6px !important;
}

/* Sidebar Logout Button Styling matching Image 1 exactly */
.st-key-menu_logout,
.st-key-menu_logout > div {
    width: 100% !important;
}
.st-key-menu_logout button,
.st-key-menu_logout [data-testid="stBaseButton-secondary"] {
    background-color: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 10px 16px !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 10px !important;
    width: 100% !important;
    height: auto !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
}
.st-key-menu_logout button:hover,
.st-key-menu_logout [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: #ffffff !important;
    border: 1px solid var(--border) !important;
}

.profile-card-text { flex: 1 !important; overflow: hidden !important; min-width: 0 !important; }
.profile-card-name {
    font-weight: 600 !important;
    font-size: 13.5px !important;
    color: var(--text) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
.profile-card-plan { font-size: 11px !important; color: var(--text-muted) !important; margin-top: 1px !important; }

/* Grid icon button (⊞) */
.st-key-profile_trigger button,
.st-key-profile_trigger [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    font-size: 18px !important;
    padding: 4px 8px !important;
    border-radius: 6px !important;
    width: auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background-color 0.15s ease !important;
}
.st-key-profile_trigger button:hover,
.st-key-profile_trigger [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Search chats button */
.st-key-search_chats_btn button,
.st-key-search_chats_btn [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text-muted) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 6px 12px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 400 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: background-color 0.15s ease, color 0.15s ease !important;
}
.st-key-search_chats_btn button:hover,
.st-key-search_chats_btn [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: var(--text) !important;
    border: none !important;
}

/* Logout button inside popover */
.st-key-menu_logout button,
.st-key-menu_logout [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text) !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: background-color 0.15s !important;
}
.st-key-menu_logout button:hover,
.st-key-menu_logout [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    border: none !important;
}

/* ── Light theme specific fixes ── */

/* Sidebar hover: keep text dark (not white) */
[data-testid="stSidebar"] .stButton button:hover,
[data-testid="stSidebar"] .stButton [data-testid="stBaseButton-secondary"]:hover {
    color: #0d0d0d !important;
    background-color: var(--hover) !important;
}

/* Popover (···) trigger button */
[data-testid="stSidebar"] [data-testid="stPopover"] button {
    background-color: transparent !important;
    color: #676767 !important;
}
[data-testid="stSidebar"] [data-testid="stPopover"] button:hover {
    background-color: var(--hover) !important;
    color: #0d0d0d !important;
}

/* Delete button in popover */
[class*="st-key-del_"] button { color: #e74c3c !important; background-color: transparent !important; }
[class*="st-key-del_"] button:hover { background-color: rgba(231,76,60,0.1) !important; }

/* Copy emoji button */
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button {
    color: #676767 !important;
    background-color: transparent !important;
}
[data-testid="stMainBlockContainer"] [class*="st-key-copy_"] button:hover {
    background-color: var(--hover) !important;
    color: #0d0d0d !important;
}

/* Profile grid ⊞ button */
.st-key-profile_trigger button {
    color: #676767 !important;
    background-color: transparent !important;
}
.st-key-profile_trigger button:hover {
    background-color: var(--hover) !important;
    color: #0d0d0d !important;
}

/* History item hover text color */
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.history-item-row) button:hover,
[data-testid="stSidebar"] div[data-testid="element-container"] > div[data-testid="stVerticalBlock"]:has(.active-chat-row) button:hover {
    color: #0d0d0d !important;
}

/* All sidebar buttons: transparent background, no border, no box-shadow */
[data-testid="stSidebar"] button,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] button:hover,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--hover) !important;
    color: #0d0d0d !important;
    border: none !important;
}

/* Delete button inside popover: render in red text */
[class*="st-key-del_"] button,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"] {
    color: #ff4b4b !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
[class*="st-key-del_"] button:hover,
[class*="st-key-del_"] [data-testid="stBaseButton-secondary"]:hover {
    background-color: rgba(255, 75, 75, 0.1) !important;
    color: #ff4b4b !important;
    border: none !important;
}

/* Sidebar footer container flex columns */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="element-container"] {
    margin: 0 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 8px !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: auto !important;
    flex: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
/* Username column should expand to take remaining space */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"]:nth-child(2) {
    flex: 1 !important;
    min-width: 0 !important;
}
/* Popover column on the right */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"]:has(.sidebar-footer-container) [data-testid="stHorizontalBlock"] [data-testid="column"]:nth-child(3) {
    flex: 0 0 auto !important;
}

/* Hide Streamlit Popover Chevron icons (targets material expand_more and expand_less icons) */
[data-testid="stSidebar"] [data-testid="stPopover"] button div[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="stPopover"] button span[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="stPopover"] button [class*="eucf0wj1"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button div[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button span[aria-hidden="true"],
[data-testid="stSidebar"] [data-testid="column"]:last-child button [class*="eucf0wj1"],
[class*="eucf0wj1"] {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    visibility: hidden !important;
    opacity: 0 !important;
}
</style>
"""

def apply_theme():
    theme = st.session_state.get("theme", "dark")
    st.markdown(DARK_CSS if theme == "dark" else LIGHT_CSS, unsafe_allow_html=True)
