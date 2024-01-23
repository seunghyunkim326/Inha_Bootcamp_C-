#include <iostream>
using namespace std;
int main()
// {
//     std::cout << "집에 가고싶어" ;
// }

{
    int i0;
    int i1;
    int sum;

    int ia;
    double a;
    const double PI=3.14;

    cout << "i0의 값을 입력하세요 : " << endl;
    cin >> i0;
    cout << "당신은 i0을 위해서 " << i0 << "를 입력했어요" << endl;
    
    cout << "i0의 값을 입력하세요 : " << endl;
    cin >> i0;
    cout << "당신은 i1을 위해서 " << i1 << "를 입력했어요" << endl;
    
    sum = i0 + i1;

    ia = static_cast<double>(i0)/static_cast<double>(i1);
    a = static_cast<double>(i0)/static_cast<double>(i1);
    cout << "i0/i1=" << a << endl;
    cout << "a/PI=" << a/PI << endl;
    cout << "ia=i0/i1" << ia << endl;

    cout << "i0+i1=" << sum << endl;

    return 0;
}