#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int C;
    cin >> C;

    string output;

    for (int caso = 0; caso < C; caso++) {

        long long N;
        cin >> N;

        long long izquierda = 1;
        long long derecha = N;

        long long respuesta = -1;

        // Suma de todas las casas
        __int128 sumaTotal = (__int128)N * (N + 1) / 2;

        while (izquierda <= derecha) {

            long long medio =
                izquierda + (derecha - izquierda) / 2;

            // Casas a la izquierda de medio
            __int128 sumaIzquierda =
                (__int128)medio * (medio - 1) / 2;

            // Casas desde medio+1 hasta N
            __int128 sumaDerecha =
                sumaTotal -
                (__int128)medio * (medio + 1) / 2;

            if (sumaIzquierda == sumaDerecha) {
                respuesta = medio;
                break;
            }

            if (sumaIzquierda < sumaDerecha) {
                izquierda = medio + 1;
            }
            else {
                derecha = medio - 1;
            }
        }

        if (respuesta == -1) {
            output += "NO\n";
        }
        else {
            output += to_string(respuesta) + "\n";
        }
    }

    cout << output;

    return 0;
}