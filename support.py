# Import necessary library
from IPython.display import display, Markdown

# Define the HTML-like markup with the images in a row and support information
markup_content = """
# Eventos App Support Page

<div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px;">
    <img src='/mnt/data/Apple iPhone 11 Screenshot 0.png' alt='Screenshot 0' style="width: 30%;">
    <img src='/mnt/data/Apple iPhone 11 Screenshot 1.png' alt='Screenshot 1' style="width: 30%;">
    <img src='/mnt/data/Apple iPhone 11 Screenshot 2.png' alt='Screenshot 2' style="width: 30%;">
</div>

## Support Information

Welcome to the **Eventos App Support Page**. If you encounter any issues or have questions about using the app, please feel free to reach out.

### Contact Information
- **Email**: [alfredojr@alfredoamezcua.com](mailto:alfredojr@alfredoamezcua.com)
- **Support Hours**: Monday to Friday, 9:00 AM to 5:00 PM (PST)

We strive to respond to all inquiries within 1-2 business days.
"""

# Display the formatted content
display(Markdown(markup_content))
