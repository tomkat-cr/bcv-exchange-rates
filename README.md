# bcv-exchange-rates

![BCV Exchange Rates](./assets/bcv.echange.rates.banner.010.png)

API to get BCV (Banco Central de Venezuela) currency exchange rates.

[English](#english) | [Español](#español)

[![Version](https://img.shields.io/badge/version-1.1.1-blue.svg)](https://github.com/tomkat-cr/cop-exchange-rates)
[![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


## English

API to get Banco Central de Venezuela (BCV) currency exchange rates with Python and scrapping the BCV website [bcv.org.ve](https://WWW.bcv.org.ve). Includes daily currency exchange between Venezuelan Bolivar and US Dollar, Euro, Japanese Yen, Russian Ruble, Chinese Yuan and Turkish Lira.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Development Commands](#development-commands)
  - [Quick Reference](#quick-reference)
  - [Setup and Maintenance](#setup-and-maintenance)
- [Usage](#usage)
  - [CLI Version](#cli-version)
  - [As Python Module](#as-python-module)
  - [Production API](#production-api)
- [Response Format](#response)
- [What is an API?](#what-is-an-api)
- [What does API mean?](#what-does-api-mean)

### Prerequisites

- Python 3.9 - 3.13
- Poetry (for the package dependency management)
- Git
- Make
- jq (optional, for pretty JSON output)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/tomkat-cr/bcv-exchange-rates.git
cd bcv-exchange-rates
make install
```

### Development Commands

All development commands are available through the Makefile. Use `make` or `make all` to see available commands.

#### Quick Reference

| Command | Description |
|---------|-------------|
| `make install` | Install project dependencies with Poetry |
| `make clean` | Clean build artifacts and cache |
| `make update` | Update dependencies and rebuild environment |
| `make test` | Run all tests with pytest |
| `make run` | Run CLI version (outputs exchange rates as JSON) |
| `make run_module` | Run the module directly with Python (same as `make run`) |
| `make run_vercel` | Run local development server with Vercel |
| `make deploy_prod` | Deploy to production (Vercel) |
| `make rename_staging` | Rename staging deployment |
| `make pypi-build` | Build package for PyPI |
| `make pypi-publish-test` | Publish to test PyPI |
| `make pypi-publish` | Publish to production PyPI |

#### Setup and Maintenance

```bash
# Install dependencies
make install

# Clean build artifacts and cache
make clean

# Update dependencies and rebuild environment
make update
```

#### Testing

```bash
# Run all tests
make test
```

#### Running the Application

```bash
# Run the CLI version (outputs exchange rates as JSON)
make run

# Run the module directly (same as "make run")
make run_module

# Run local development server with Vercel
make run_vercel
```

#### Deployment

```bash
# Deploy to production (Vercel)
make deploy_prod

# Rename staging deployment (requires deployment URL as parameter)
make rename_staging <deployment-url>
```

#### Publishing to PyPI

```bash
# Build package for PyPI
make pypi-build

# Publish to test PyPI
make pypi-publish-test

# Publish to production PyPI
make pypi-publish
```

### Usage

#### Command Line Interface

Run the CLI to get current exchange rates:

```bash
make run
```

Or run the module directly:

```bash
python -m bcv_exchange_rates.index cli
```

#### As a Python Module

```python
from bcv_exchange_rates.bcv import get_bcv_exchange_rates

# Get current exchange rates
rates = get_bcv_exchange_rates()
print(rates)
```

### Production API

```url
https://bcv-exchange-rates.vercel.app/get_bcv_exchange_rates
```

### Response

```json
{
  "error": false,
  "error_message": [],
  "data": {
    "euro": {
      "symbol": "EUR",
      "value": "19,39949699"
    },
    "yuan": {
      "symbol": "CNY",
      "value": "2,67429452"
    },
    "lira": {
      "symbol": "TRY",
      "value": "0,98005430"
    },
    "rublo": {
      "symbol": "RUB",
      "value": "0,25213624"
    },
    "dolar": {
      "symbol": "USD",
      "value": "18,39460000"
    },
    "effective_date": "Viernes, 06 Enero  2023",
    "run_timestamp": "2023-01-06 11:55:42 UTC"
  }
}
```

### What is an API?

APIs are mechanisms that allow two software components or programs to communicate with each other using a set of definitions and protocols. For example, this bcv-exchange-rates API returns daily exchange rate data taken from the BCV website. An application on your phone that needs to do currency conversion "talks" to this system through the APIs and shows you daily exchange updates for dollar, euro, yen, ruble, yuan, and lira on your phone.

### What does API mean?

API stands for "Application Programming Interface". In the context of APIs, the word "application" refers to any software or program with distinct and/or independent functions. The interface can be thought of as a service contract between two applications. This contract defines how they communicate with each other through requests and responses. Your API documentation should contain information about how developers should structure those requests and responses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

This project is developed and maintained by [Carlos J. Ramirez](https://github.com/tomkat-cr). For more information or to contribute to the project, visit [BCV Exchange Rates](https://github.com/tomkat-cr/bcv-exchange-rates).

Happy Coding!

<br/>

------------------------------
<br/>

## Español

API Dólar Oficial del BCV (Banco Central de Venezuela). Desarrollada en Python y haciendo web scrapping del sitio Web [bcv.org.ve](https://WWW.bcv.org.ve) en vista de la falta de una API oficial de la institución.<br/>
Incluye actualizaciones de cambio monetarias diarias de: dólar norteamericano, euro, yen japonés, rublo ruso, yuan chino y liras turcas.

### Prerrequisitos

- Python 3.9 - 3.13
- Poetry (para gestión de dependencias)
- jq (opcional, para salida JSON formateada)

### Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/tomkat-cr/bcv-exchange-rates.git
cd bcv-exchange-rates
make install
```

### Comandos de Desarrollo

Todos los comandos de desarrollo están disponibles a través del Makefile. Usa `make` o `make all` para ver los comandos disponibles.

#### Referencia Rápida

| Comando | Descripción |
|---------|-------------|
| `make install` | Instalar dependencias del proyecto con Poetry |
| `make clean` | Limpiar artefactos de construcción y cache |
| `make update` | Actualizar dependencias y reconstruir entorno |
| `make test` | Ejecutar todas las pruebas con pytest |
| `make run` | Ejecutar versión CLI (muestra la respuesta de las tasas de cambio como JSON) |
| `make run_module` | Ejecutar el módulo directamente con Python (es lo mismo que `make run`) |
| `make run_vercel` | Ejecutar servidor de desarrollo local con Vercel |
| `make deploy_prod` | Desplegar a producción (Vercel) |
| `make rename_staging` | Renombrar despliegue de staging |
| `make pypi-build` | Construir paquete para PyPI |
| `make pypi-publish-test` | Publicar en PyPI de prueba |
| `make pypi-publish` | Publicar en PyPI de producción |

#### Configuración y Mantenimiento

```bash
# Instalar dependencias
make install

# Limpiar artefactos de construcción y cache
make clean

# Actualizar dependencias y reconstruir entorno
make update
```

#### Pruebas

```bash
# Ejecutar todas las pruebas
make test
```

#### Ejecutar la Aplicación

```bash
# Ejecutar la versión CLI (muestra tasas de cambio como JSON)
make run

# Ejecutar el módulo directamente (igual que "make run")
make run_module

# Ejecutar servidor de desarrollo local con Vercel
make run_vercel
```

#### Despliegue

```bash
# Desplegar a producción (Vercel)
make deploy_prod

# Renombrar despliegue de staging (requiere URL de despliegue como parámetro)
make rename_staging <deployment-url>
```

#### Publicar en PyPI

```bash
# Construir paquete para PyPI
make pypi-build

# Publicar en PyPI de prueba
make pypi-publish-test

# Publicar en PyPI de producción
make pypi-publish
```

### Uso

#### Interfaz de Línea de Comandos

Ejecuta el CLI para obtener tasas de cambio actuales:

```bash
make run
```

O ejecuta el módulo directamente:

```bash
python -m bcv_exchange_rates.index cli
```

#### Como Módulo de Python

```python
from bcv_exchange_rates.bcv import get_bcv_exchange_rates

# Obtener tasas de cambio actuales
rates = get_bcv_exchange_rates()
print(rates)
```

### API de Producción

```url
https://bcv-exchange-rates.vercel.app/get_bcv_exchange_rates
```

### Respuesta

```json
{
  "error": false,
  "error_message": [],
  "data": {
    "euro": {
      "symbol": "EUR",
      "value": "19,39949699"
    },
    "yuan": {
      "symbol": "CNY",
      "value": "2,67429452"
    },
    "lira": {
      "symbol": "TRY",
      "value": "0,98005430"
    },
    "rublo": {
      "symbol": "RUB",
      "value": "0,25213624"
    },
    "dolar": {
      "symbol": "USD",
      "value": "18,39460000"
    },
    "effective_date": "Viernes, 06 Enero  2023",
    "run_timestamp": "2023-01-06 11:55:42 UTC"
  }
}
```

### ¿Qué es una API?

Las API son mecanismos que permiten a dos componentes de software o programas comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, esta API bcv-exchange-rates devuelve datos de tasas de cambios diarias tomadas del sitio web del BCV. Una aplicación de su teléfono que necesite hacer conversión monetaria "habla" con este sistema a través de las API y le muestra en su teléfono las actualizaciones del cambio diarias de dólares, euros, yenes, rublos, yuanes y liras.

### ¿Qué significa API?

API son las siglas de "interfaz de programación de aplicaciones". En el contexto de las API, la palabra aplicación se refiere a cualquier software o programa con funciones distintas y/o independientes. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define cómo se comunican entre sí mediante solicitudes y respuestas. La documentación de su API debe contener información sobre cómo los desarrolladores deben estructurar esas solicitudes y respuestas.

## License

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo [LICENSE](LICENSE) para más detalles.

## Credits

Este proyecto es desarrollado y mantenido por [Carlos J. Ramirez](https://github.com/tomkat-cr). Para más información o para contribuir al proyecto, visite [BCV Exchange Rates](https://github.com/tomkat-cr/bcv-exchange-rates).

¡Sé Feliz Programando!