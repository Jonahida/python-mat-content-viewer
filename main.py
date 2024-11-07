import tkinter as tk
from tkinter import filedialog, messagebox
from scipy.io import loadmat

def browse_file():
    """Open file dialog to browse and select a file."""
    file_path = filedialog.askopenfilename(title="Select a File", 
                                           filetypes=[("MAT Files", "*.mat"), ("All Files", "*.*")])
    if file_path:
        path_label.config(text=file_path)  # Display the selected file path in the label

def load_and_display_content():
    """Load the .mat file and display its content."""
    file_path = path_label.cget("text")  # Get the current file path from the label
    
    if file_path == "No file selected":
        messagebox.showwarning("No file", "Please select a file first.")
        return
    
    try:
        # Load .mat file content using scipy
        data = loadmat(file_path)
        
        # Display the contents in a text box or label (for simplicity, just showing keys)
        content = "\n".join([f"{key}: {type(value)}" for key, value in data.items()])
        content_label.config(text=content)
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the file:\n{e}")

# Create the main window
root = tk.Tk()
root.title("File Path Selector and Content Viewer")

# Create a button that opens the file dialog
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Label to display the selected file path
path_label = tk.Label(root, text="No file selected", width=50, height=2, anchor="w")
path_label.pack(pady=10)

# Button to load and display the content of the file
run_button = tk.Button(root, text="Run", command=load_and_display_content)
run_button.pack(pady=10)

# Label to display the content of the file (e.g., keys of the .mat file)
content_label = tk.Label(root, text="File content will appear here.", width=100, height=10, anchor="w", justify="left")
content_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
