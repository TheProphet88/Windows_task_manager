from django import template
import datetime
import psutil

register = template.Library()


@register.filter('date_converter')
def convert_timestamp_to_time(timestamp):
    """" ეს ფუნქცია, epoch დროს აკონვერტირებს, human readable დროზე."""
    
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d | %H:%M:%S")


    
