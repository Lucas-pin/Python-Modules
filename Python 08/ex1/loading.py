import sys
import os
import importlib.metadata

# Definición de paquetes con bandera de obligatoriedad (True/False)
PACKAGES = [
    ("pandas", "Data manipulation ready", True),
    ("numpy", "Numerical computation ready", True),
    ("requests", "Network access ready", False),  # Opcional
    ("matplotlib", "Visualization ready", True),
]


def detect_environment():
    """Detecta si el script se está ejecutando mediante Poetry o pip/venv."""
    if os.environ.get("POETRY_ACTIVE") == "1":
        return "Poetry Environment (Isolated lockfile-based)"
    elif sys.prefix != sys.base_prefix:
        return "Standard Virtualenv (pip-based)"
    return "Global Python System"


def check_package(pkg_name):
    """Obtiene la versión del paquete o devuelve None si no existe."""
    try:
        return importlib.metadata.version(pkg_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def fetch_api_data():
    """Consulta una API externa para obtener datos reales."""
    import requests
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&hourly=temperature_2m"
    response = requests.get(url, timeout=4)
    response.raise_for_status()
    data = response.json()
    return data["hourly"]["temperature_2m"]


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing_core = []
    has_requests = False

    # Verificación de dependencias respetando el orden de salida requerido
    for pkg, desc, is_required in PACKAGES:
        version = check_package(pkg)
        if version:
            print(f"[OK] {pkg} ({version}) - {desc}")
            if pkg == "requests":
                has_requests = True
        else:
            if is_required:
                print(f"[MISSING] {pkg} - Not installed")
                missing_core.append(pkg)

    # Detener ejecución si faltan dependencias obligatorias
    if missing_core:
        print("\n" + "=" * 50)
        print(" [ERROR] Missing core dependencies detected!")
        print("=" * 50)
        print("\nTo install dependencies using PIP:")
        print("  pip install -r requirements.txt")
        print("\nTo install dependencies using POETRY:")
        print("  poetry install")
        print("=" * 50)
        sys.exit(1)

    env_type = detect_environment()
    print(f"\n[ENV INFO] Running on: {env_type}")

    # Importaciones dinámicas para procesamiento y gráficos
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    using_api = False
    raw_data = None

    # Intentar obtener datos reales si requests está instalado
    if has_requests:
        try:
            print("Connecting to Matrix external stream (API)...")
            api_data = fetch_api_data()
            raw_data = np.array(api_data)
            using_api = True
            print(f"Successfully retrieved {len(raw_data)} data points from API!")
        except Exception as e:
            print(f"API connection failed ({e}). Falling back to NumPy simulation...")

    # Simulación por defecto con NumPy si no hay requests o falló la API
    if not using_api:
        num_points = 1000
        print(f"Processing {num_points} simulated data points...")
        np.random.seed(42)
        raw_signal = np.random.normal(loc=100, scale=15, size=num_points)
        noise = np.sin(np.linspace(0, 10 * np.pi, num_points)) * 20
        raw_data = raw_signal + noise

    # Manipulación de datos con Pandas y NumPy
    df = pd.DataFrame({"Signal": raw_data})
    df["Rolling_Mean"] = df["Signal"].rolling(window=10 if using_api else 30).mean()

    # Generación de la visualización
    print("Generating visualization...")
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        df["Signal"],
        color="#00FF66",
        alpha=0.4,
        label="Live API Stream" if using_api else "Raw Matrix Signal"
    )
    ax.plot(
        df["Rolling_Mean"],
        color="#00FF00",
        linewidth=2,
        label="Filtered Stream"
    )

    title = "Matrix Live API Data Analysis" if using_api else "Matrix Data Stream Analysis"
    ax.set_title(title, color="#00FF00", fontsize=14)
    ax.set_xlabel("Time Frame", color="#00FF00")
    ax.set_ylabel("Signal Level", color="#00FF00")
    ax.grid(True, color="#003300", linestyle="--")
    ax.legend(facecolor="black", edgecolor="#00FF00")

    output_filename = "matrix_analysis.png"
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")


if __name__ == "__main__":
    main()