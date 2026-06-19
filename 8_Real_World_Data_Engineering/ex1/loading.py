#!/usr/bin/env python3

import sys
import os
from importlib import metadata, import_module


def warn_global_environment() -> None:
    """
        Tell user that it is not in a venv
    """
    print(f"Current Python: {os.path.realpath(sys.executable)}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print()
    print("To enter a virtual environment, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate   # On Unix")
    print("matrix_env\\Scripts\\activate    # On Windows")
    print()
    print("Then run this program again.")


def check_dependency(package_name: str) -> bool:
    """
        Check if a dependency is already installed and import
        it if so
    """
    packages_description = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready'
    }
    try:
        import_module(package_name)
        version = metadata.version(package_name)
        desc = packages_description[package_name]
        print(f"[OK] {package_name} ({version}) - {desc}")
        return True
    except ModuleNotFoundError:
        print(f"[MISSING] {package_name} is not installed")
    return False


def missing_dependencies() -> None:
    """
        Print instructions for installing dependencies using
        pip and poetry
    """
    print("For installing missing dependencies run:")
    print("- pip:")
    print("    % pip install -r requirements.txt    # Install all "
          "dependencies inside the requirements.txt file with very ")
    print("                                           little "
          "dependency conflict resolution")
    print()
    print("- poetry:")
    try:
        metadata.version('poetry')
    except ModuleNotFoundError:
        print("    % pip install poetry")
    print("    % poetry lock        # Does the dependency management, by "
          "locking dependencies version for environment consistency, ")
    print("                           also blocks two packages from "
          "requiring conflicting versions of a third one")
    print("    % poetry install     # Will automatically run poetry lock, to "
          "guarantee that dependencies are managed and install the ")
    print("                           missing ones")


def generate_data() -> None:
    """
        Simulate Matrix data using numpy, analyze with pandas, plot with
        matplotlib.
    """
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    np = import_module('numpy')
    pd = import_module('pandas')
    plt = import_module('matplotlib.pyplot')

    noise = np.random.normal(0, 0.5, 1000)

    time_steps = np.arange(1000)
    sine_wave = np.sin(time_steps * 0.05)
    noisy_sine = sine_wave + noise

    df = pd.DataFrame({
        'Time': time_steps,
        'Noise': noise,
        'Noisy_Sine': noisy_sine
    })

    plt.figure(figsize=(10, 5))

    plt.plot(df['Time'], df['Noisy_Sine'], color='green', alpha=0.8,
             label='Noisy Sine Wave')
    plt.plot(df['Time'], df['Noise'], color='red', alpha=0.3,
             label='Noise')

    plt.title("Matrix Signal Analysis: Sine Wave with Noise Overlay")
    plt.xlabel("Step")
    plt.ylabel("Amplitude")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()

    output_filename = "matrix_analysis.png"
    plt.savefig(output_filename)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        warn_global_environment()
    else:
        print()
        print("LOADING STATUS: Loading programs...")
        print()
        print("Checking dependencies:")
        print()
        dependencies = ['pandas', 'numpy', 'matplotlib']
        all_dependencies_found = True
        for dependency in dependencies:
            if not check_dependency(dependency):
                all_dependencies_found = False
        print()
        if all_dependencies_found:
            generate_data()
        else:
            missing_dependencies()
