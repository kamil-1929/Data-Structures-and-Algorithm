# Function to check if the current environment is Google Colab
def is_google_colab():
    try:
        import google.colab
        return True
    except:
        return False
    
    
