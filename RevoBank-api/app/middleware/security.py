from flask import request, abort
import ipaddress
import re

class SecurityMiddleware:
    @staticmethod
    def validate_input(input_string, pattern=None):
        """
        Validate and sanitize input
        """
        if not input_string:
            return None
        
        # Remove potential XSS characters
        sanitized = re.sub(r'[<>&\']', '', input_string)
        
        # Optional regex pattern validation
        if pattern and not re.match(pattern, sanitized):
            return None
        
        return sanitized
    
    @staticmethod
    def check_ip_reputation(ip_address):
        """
        Basic IP reputation check
        In production, integrate with IP reputation services
        """
        try:
            ip = ipaddress.ip_address(ip_address)
            
            # Block private and reserved IP ranges
            if ip.is_private or ip.is_reserved:
                return False
            
            return True
        except ValueError:
            return False

# Middleware usage in routes
@app.before_request
def security_checks():
    ip_address = request.remote_addr
    
    if not SecurityMiddleware.check_ip_reputation(ip_address):
        abort(403, description="Access Denied")