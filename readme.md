# Introduction

LogycaTest is a Rest API Service built to creating or updating a register with information related to inventories, clients, branch offices and products. Service was deployed in Azure app service, and it has a connection with an Azure Database for PostgreSQL. Right now, you can find the service in [Logyca](https://logycatestapi.azurewebsites.net/). 

Also, you can find how to use the [Logyca](https://logycatestapi.azurewebsites.net/) API in the main of the service. I hope that you enjoy these docs and if you have any question, you can send an email to Diegorojascifuentes@gmail.com, you will get an answer 
as soon as possible.

## Authorization

Due to this just a test, API does not have  any API Key or paramether to authorize its use.  

## GET requests
`Returns customers` [api/Cliente/](https://logycatestapi.azurewebsites.net/api/Cliente/) <br/>
`Returns branch offices.` [api/Sucursales/](https://logycatestapi.azurewebsites.net/api/Sucursales/) <br/>
`Returns products.` [api/Producto/](https://logycatestapi.azurewebsites.net/api/Producto/) <br/>
`Returns inventory registers.` [api/Registro/](https://logycatestapi.azurewebsites.net/api/Registro/) <br/>
`Returns inventories.` [api/Inventario/](https://logycatestapi.azurewebsites.net/api/Inventario/) <br/>
`Returns registers.` [api/AllRegistro/](https://logycatestapi.azurewebsites.net/api/AllRegistro/) <br/>
`Returns registers by client.` [api/AllRegistro/byCliente/{GLN_cliente}](https://logycatestapi.azurewebsites.net/api/AllRegistro/byCliente/{GLN_cliente}) <br/>
`Returns registers by sucursal.` [api/AllRegistro/bySucursal/{GLN_sucursal}](https://logycatestapi.azurewebsites.net/api/AllRegistro/bySucursal/{GLN_sucursal}) <br/>
`Returns registers by Producto.` [api/AllRegistro/byProducto/{GLN_producto}](https://logycatestapi.azurewebsites.net/api/AllRegistro/byProducto/{GLN_producto}) <br/>

## POST requests
`Post new register` [api/CreateRegistro/](https://logycatestapi.azurewebsites.net/api/CreateRegistro/) <br/>
### Body :
```body
    {
    "Inventario": {
        "Cliente": {
        "GLN_Cliente": $input [INT]
        },
        "Sucursal": {
        "GLN_Sucrusal": $input [INT]
        },
        "Fecha": $input [Date: aaaa-mm-dd]
    },
    "Producto": {
        "Gtin_Producto": $input [INT],
        "PrecioUnidad": $input [DOUBLE]
        },
    "Inventario_Final": $input [INT]
    }
```
## PUT requests
`Update a register exist related to client, branch office and product.` [api/UpdateRegistro/](https://logycatestapi.azurewebsites.net/api/UpdateRegistro/) <br/>
### Body :
```body
    {
    "Inventario": {
        "Cliente": {
        "GLN_Cliente": $input [INT]
        },
        "Sucursal": {
        "GLN_Sucrusal": $input [INT]
        },
        "Fecha": $input [Date: aaaa-mm-dd]
    },
    "Producto": {
        "Gtin_Producto": $input [INT],
        "PrecioUnidad": $input [DOUBLE]
        },
    "Inventario_Final": $input [INT]
    }
```

## Responses

All endpoints return a JSON  representation like a response to the resource requested.

## Status Codes

LogycaTest returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` | Request completed.|
| 201 | `CREATED` | New register  has been created. |
| 202 | `ACCEPTED` | Register has been updated. |
| 400 | `BAD REQUEST` | There is a problem with the body request. | 
| 409 | `CONFLICT` | Register exists, PUT request have to be used to update the register. | 
| 404 | `NOT FOUND` | Register does not exist. |
| 500 | `INTERNAL SERVER ERROR` | There is a problem with the server. | 