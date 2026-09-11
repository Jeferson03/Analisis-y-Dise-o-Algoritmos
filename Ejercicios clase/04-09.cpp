#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Leer datos
    int n;
    bool hecho = false;
    cin >> n;


    // Resolver problema
    for (int i=2; i<n; i++) {
        int sumaIzq = 0;
        for (int j=1; j<i; j++) {
            sumaIzq += j;
        }
        int sumaDer = 0;
        for (int k=i+1; k<=n; k++) {
            sumaDer += k;
        }
        if (sumaIzq == sumaDer) {
             cout << i ;
             hecho = true;
             break;
        }
    }
    if (hecho == false) {
        cout << "NO" ;
    }
 

    return 0;
}