import subprocess

def run_linux_command(command_args: list[str]) -> str:
    """
    Executes a predefined Linux command safely and returns its output.
    Raises an Exception if the command fails.
    """
    try:
        result = subprocess.run(
            command_args, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        raise Exception(f"Command execution failed: {error_msg}")
    except FileNotFoundError:
        raise Exception("Requested command utility not found on this system.")