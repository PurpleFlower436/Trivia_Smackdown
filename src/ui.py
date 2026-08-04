from rich.console import Console

from rich.panel import Panel

console = Console()

# Centralized Theme
color_instruction = "bold slate_blue"
color_question    = "bold cyan"
color_choice      = "gold3"
color_error       = "bold red"


def show_question(question_dict):
    """
    Renders a stylized question block and its multiple-choice options.
    
    Extracts the core question text and wraps it inside a modern cyan Panel, 
    then iterates through all corresponding dictionary choice keys to output 
    them using a cohesive amber/yellow theme.

    :param question_dict: dict containing the keys 'question' (str) and 'choices' (dict)
    :return: None
    """
    # 1. Print header
    console.print(f"[{color_instruction}]📋 Question Block:[/{color_instruction}]")
    
    # 2. Print question text in modern cyan panel
    question_text = f"[{color_question}]{question_dict['question']}[/{color_question}]"
    console.print(Panel(question_text, border_style="cyan"))
    
    # 3. Print the answer choice options in clean amber/yellow
    for key, value in question_dict["choices"].items():
        console.print(f"[[{color_choice}]{key}[/{color_choice}]] {value}")
    console.print("") # Blank line for cleaner spacing

def show_error(message):
    """
    Renders error messages safely onto the active console.
    
    Applies the centralized error theme style tag to highlight incorrect 
    inputs or processing failures cleanly to the user.

    :param message: str containing the raw error statement text to display
    :return: None
    """
    console.print(f"[{color_error}]{message}[/{color_error}]")





def prompt_style(message_text):
    """
    Formats a raw text string with the centralized instruction theme color.
    
    Wraps input strings inside rich color tags so they map natively to 
    the active terminal shell instance when evaluated downstream.

    :param message_text: str representing the prompt or raw guidepost question
    :return: str styled text with the proper terminal color codes applied
    """
    return f"[{color_instruction}]{message_text}[/{color_instruction}]"

def show_title(title_text):
    """
    Renders a prominent text title card at the start of a main game sequence.
    
    Wraps game section headers into a centered structural panel featuring 
    custom emoji icons and a bold magenta background design layout.

    :param title_text: str representing the main heading or game title string
    :return: None
    """
    console.print(Panel(f"⚔️ [bold magenta]{title_text}[/bold magenta] ⚔️", expand=False, border_style="magenta"))
