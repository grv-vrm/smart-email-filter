def classify_email_priority(email_entry):
    """
    Classify an email into High, Medium, or Low priority
    based on simple rules (subject, sender, etc.)
    """
    subject = email_entry.get('subject', '').lower()
    sender = email_entry.get('sender', '').lower()

    high_priority_keywords = ["urgent", "asap", "immediate", "important"]
    low_priority_keywords = ["newsletter", "promotion", "unsubscribe", "sale"]

    # Check for high-priority keywords
    if any(word in subject for word in high_priority_keywords):
        return "High"
    
    # Check for important senders (customize if you want)
    important_senders = ["boss@company.com", "hr@company.com"]
    if any(imp in sender for imp in important_senders):
        return "High"

    # Check for low-priority keywords
    if any(word in subject for word in low_priority_keywords):
        return "Low"

    # Default is Medium
    return "Medium"
