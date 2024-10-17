// Cajero Automático Simulado en Puro JavaScript
let saldo = 1000; // Saldo inicial

function mostrarMenu() {
    console.log("\n--- Cajero Automático ---");
    console.log("1. Consultar saldo");
    console.log("2. Retirar dinero");
    console.log("3. Depositar dinero");
    console.log("4. Salir");
    let opcion = prompt("Seleccione una opción: ");
    return opcion;
}

function consultarSaldo() {
    console.log(`Su saldo actual es: $${saldo}`);
}

function retirarDinero() {
    let monto = parseFloat(prompt("Ingrese el monto a retirar: "));
    if (isNaN(monto) || monto <= 0) {
        console.log("Monto no válido.");
    } else if (monto > saldo) {
        console.log("Fondos insuficientes.");
    } else {
        saldo -= monto;
        console.log(`Ha retirado $${monto}. Su saldo actual es $${saldo}`);
    }
}

function depositarDinero() {
    let monto = parseFloat(prompt("Ingrese el monto a depositar: "));
    if (isNaN(monto) || monto <= 0) {
        console.log("Monto no válido.");
    } else {
        saldo += monto;
        console.log(`Ha depositado $${monto}. Su saldo actual es $${saldo}`);
    }
}

function iniciarCajero() {
    let continuar = true;

    while (continuar) {
        let opcion = mostrarMenu();

        switch (opcion) {
            case '1':
                consultarSaldo();
                break;
            case '2':
                retirarDinero();
                break;
            case '3':
                depositarDinero();
                break;
            case '4':
                console.log("Gracias por usar el cajero. ¡Hasta luego!");
                continuar = false;
                break;
            default:
                console.log("Opción no válida. Intente de nuevo.");
        }
    }
}

// Simular prompt en Node.js si es necesario
function prompt(question) {
    const readlineSync = require('readline-sync');
    return readlineSync.question(question);
}

// Iniciar simulación del cajero
iniciarCajero();
