messages = [
    # --- SPAM messages ---
    "win money now",
    "claim your free prize",
    "cheap loans available",
    "congratulations you won",
    "free cash reward click now",
    "urgent you have been selected",
    "get rich quick guaranteed",
    "you are a winner claim your prize",
    "earn money from home free",
    "limited time offer act now",
    "click here to claim your free gift",
    "buy cheap meds online now",
    "make money fast no experience",
    "hot singles in your area",
    "special discount offer expires today",
 
    # --- NOT SPAM messages ---
    "meeting tomorrow at office",
    "project deadline reminder",
    "team lunch today",
    "can we reschedule the call",
    "please review the attached document",
    "see you at the standup",
    "let me know if you need help",
    "the report is ready for review",
    "happy birthday have a great day",
    "dinner at seven tonight",
    "call me when you are free",
    "thanks for the update",
    "are you coming to the event",
    "i will be late by ten minutes",
    "good morning how are you",
]
 
labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # spam
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # not spam
]

SPAM_KEYWORDS = [
    "win", "free", "prize", "cash", "money", "cheap",
    "offer", "click", "now", "claim", "earn", "buy",
    "urgent", "selected", "reward", "discount", "rich",
    "guaranteed", "limited", "congratulations", "hot",
    "singles", "meds", "fast", "special", "expires",
    "gift", "winner", "online", "home", "quick",
]