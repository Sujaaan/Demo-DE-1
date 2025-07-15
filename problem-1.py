AUTHENTICATED = False

def require_auth(func):
    def wrapper(*args, **kwargs):
        global AUTHENTICATED
        if not AUTHENTICATED:
            print("Access denied. Please log in.")
            return
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_dashboard():
    print("Welcome to your dashboard!")

@require_auth
def logout():
    global AUTHENTICATED
    AUTHENTICATED = False
    print("Logged out.")

def login():
    global AUTHENTICATED
    AUTHENTICATED = True
    print("Logged in.")

if __name__ == "__main__":
    view_dashboard()  # Should be denied
    login()           # Logs in
    view_dashboard()  # Should show dashboard
    logout()          # Logs out
    view_dashboard()  # Denied again
