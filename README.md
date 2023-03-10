# bcv-exchange-rates

## English

API to get Banco Central de Venezuela (BCV) currency exchange rates with Python and scrapping the BCV website [bcv.org.ve](https://WWW.bcv.org.ve).<br/>
Includes daily currency exchange rates of US Dollar, Euro, Japanese Yen, Russian Ruble, Chinese Yuan y Turkish Lira.

## Production API call

```url
https://bcv-exchange-rates.vercel.app/get_exchange_rates
```

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

## What is an API?

APIs are mechanisms that allow two software components or programs to communicate with each other using a set of definitions and protocols. For example, this bcv-exchange-rates API returns daily exchange rate data taken from the BCV website. An application on your phone that needs to do currency conversion "talks" to this system through the APIs and shows you daily exchange updates for dollar, euro, yen, ruble, yuan, and lira on your phone.

## What does API mean?

API stands for "Application Programming Interface". In the context of APIs, the word "application" refers to any software or program with distinct and/or independent functions. The interface can be thought of as a service contract between two applications. This contract defines how they communicate with each other through requests and responses. Your API documentation should contain information about how developers should structure those requests and responses.

<br/>

------------------------------
<br/>

## Spanish

API dolar oficial del BCV (Banco Central de Venezuela). Desarrollada en Python y haciendo web scrapping del sitio Web [bcv.org.ve](https://WWW.bcv.org.ve) en vista de la falta de una API oficial de la instituci??n.<br/>
Incluye actualizaciones de cambio monetarias diarias de: d??lar norteamericano, euro, yen japon??s, rublo ruso, yuan chino y liras turcas.

## Llamada a la API de producci??n

```url
https://bcv-exchange-rates.vercel.app/get_exchange_rates
```

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

## ??Qu?? es una API?

Las API son mecanismos que permiten a dos componentes de software o programas comunicarse entre s?? mediante un conjunto de definiciones y protocolos. Por ejemplo, esta API bcv-exchange-rates devuelve datos de tasas de cambios diarias tomadas del sitio web del BCV. Una aplicaci??n de su tel??fono que necesite hacer conversi??n monetaria "habla" con este sistema a trav??s de las API y le muestra en su tel??fono las actualizaciones del cambio diarias de d??lares, euros, yenes, rublos, yuanes y liras.

## ??Qu?? significa API?

API son las siglas de "interfaz de programaci??n de aplicaciones". En el contexto de las API, la palabra aplicaci??n se refiere a cualquier software o programa con funciones distintas y/o independientes. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define c??mo se comunican entre s?? mediante solicitudes y respuestas. La documentaci??n de su API debe contener informaci??n sobre c??mo los desarrolladores deben estructurar esas solicitudes y respuestas.
