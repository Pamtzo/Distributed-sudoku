# Distributed-sudoku

Sudoku distribuido haciendo uso de el modelo ventilator-worker-sink de zmq con python.\
El problema se resuelve por profundidad de la siguiente manera:\
*El ventilator delega el trabajo a un worker\
  *El worker filtra el tablero haciendo las jugadas obligadas o descartando el tablero\
  *El worker escoge el camino con menos variantes posibles y juega una de esas variantes\
  *Si se logra la profundidad maxima el worker envia al sink el estado del tablero y vuelve al estado anterior para hacer otra jugada\
*El sink al recibir el tablero, si este no se encuentra resuelto lo envia al ventilator, si esta resulto termina la ejecución
