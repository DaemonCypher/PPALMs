// TEST.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;
class mainBank
{
private:
    float account = 0;
    float value;
    int NumDeposit = 0;
    int SaveNumWithdraw = 0;
    int SaveNumDeposit = 0;
    int NumWithdraw = 0;
    int NumMonthIntrest = 0;
public:
    void setCharge(float);
    void setWithdraw(float);
    void setDeposit(float);
    void setMonthIntrest(float);
};
class savings
{
private:
    float account = 0;
    float value;
    int NumDeposit = 0;
    int SaveNumWithdraw = 0;
    int SaveNumDeposit = 0;
    int NumWithdraw = 0;
    int NumMonthIntrest = 0;
public:
    void saveactivate(float);
    void savewithdrawl(float);
    void savedeposit(float);
    void saveproc(float);
};
class checking_account
{
private:
    double account = 0;
    double value;
    float new_amount;
    int NumDeposit = 0;
    int NumWithdraw = 0;
    int NumMonthIntrest = 0;
    int monthly_fee = 5;

public:
    void checkWithdraw(double);
    void checkwithdraw(double);
    void checkDeposit(double);
    void checkCharge(float);
    void checkMonthIntrest(float);
};

void checking_account::checkWithdraw(double withdraw)
{
    cout << "Are you here to make a withdraw on your checking account?(1/0)\n1 is for yes, and 0 is for no\n" << endl;
    cin >> withdraw;
    if (withdraw == 1)
    {
        cout << "The current value of your account is " << account << " dollars" << endl;
        cout << "Enter the amount you want to be withdrawn\n";
        cin >> value;

        if (value > 0) {
            account = account - value;
        }

        if (value > account) {
            cout << "\n";
        }
        cout << "Your current account value is " << account << " dollars" << endl;
        NumWithdraw = NumWithdraw + 1;


    }
    else
    {
        cout << "You do not want to make a withdraw\n" << endl;
    }
}
void checking_account::checkMonthIntrest(float MonthIntrest)
{
    cout << "Are you here to calculate your monthly intrest on your checking ?(1/0)\n1 is for yes, and 0 is for no\n" << endl;
    cin >> MonthIntrest;
    if (MonthIntrest == 1)
    {
        cout << "The current value of your account is " << account << " dollars" << endl;
        cout << "What is your monthly intrest rate\n";
        cin >> MonthIntrest;
        MonthIntrest = account * MonthIntrest;
        account = account + MonthIntrest;
        cout << "Current intrest generated by the monthly intrest rate is " << MonthIntrest << " dollars.\n total value of account is " << account << " dollars.\n";
        NumMonthIntrest = NumMonthIntrest + 1;
    }
    else
    {
        cout << "You do not want to make a to calculate your monthly intrest rate\n" << endl;
    }
}
void checking_account::checkCharge(float charge)
{
    int total;
    cout << "\nThe bank charges a dollar each time you use these services for your checking\n" << endl;
    total = NumDeposit + NumWithdraw + NumMonthIntrest;
    cout << "The bank will charge you " << total << " dollars" << endl;
    account = account - total;
    cout << "Your current account value is " << account << " dollars\n" << endl;
}
void checking_account::checkwithdraw(double balance)
{
    if (value < 0) {

        cout << "\nWithdraw positive numbers only.\n";

    }


    if (account < 25) {

        cout << "\nYour account is inactive\n";

    }

    if (account < 0) {

        account = account - 15;
        cout << "a 15 dollar service charge  is apply when your bank account fall under 0 \nyour new balance is: \n" << account << " dollars" << endl;

    }

    if (account - value > 0 && account - value < 25) {

        cout << "\nYour account is below $25.00. It will be deactivated\n";

    }

    account = (account - monthly_fee + (NumWithdraw * 0.1));
    cout << "\namount after monthly fee: " << account << " dollars" << endl;

}
void checking_account::checkDeposit(double deposit)
{
    cout << "Are you here to make a deposit in your checking account?(1/0)\n1 is for yes, and 0 is for no\n";
    cin >> deposit;
    if (deposit == 1)
    {
        cout << "The current value of your account is " << account << " dollars.\n" << endl;
        cout << "Enter the amount you want to be deposited\n" << endl;
        cin >> value;
        account = value + account;
        cout << "Your current account value is " << account << " dollars." << endl;
        NumDeposit = NumDeposit + 1;
    }
    else
    {
        cout << "You do not want to make a deposit\n" << endl;
    }
}

void savings::saveactivate(float active)
{
    cout << "Do you want to activate a savings account?(1/0)\n1 is for yes, and 0 is for no\n";
    cin >> active;
    if (active == 1)
    {
        cout << "The current value of your account is " << account << " dollars.\n" << endl;
        cout << "You need to have a minimum of $25 for your account to remain active. Enter the amount you want to be deposited\n" << endl;
        cin >> value;
        account = value + account;
        cout << "Your current account value is " << account << " dollars." << endl;
       
    }
    else
    {
        cout << "You do active your account.\n" << endl;

    }
}
void savings::savewithdrawl(float swithdrawl)
{
    cout << "Do you want to withdrawl money from your savings account?(1/0)\n1 is for yes, and 0 is for no\n";
    cin >> swithdrawl;
    if (swithdrawl == 1)
    {
        if (account < 25)
        {
            cout << "You may not withdrawl, you account is below $25.";
        }
        else 
        {
            cout << "The current value of your account is " << account << " dollars.\n" << endl;
            cout << "Enter the amount you want to be withdrawn.\n" << endl;
            cin >> value;
            account = value - account;
            cout << "Your current account value is " << account << " dollars." << endl;
            SaveNumWithdraw = SaveNumWithdraw + 1;//--------------------------------------------------------------------------------------------------------------------------
        }
    }
    else
    {
        cout << "You do not want to make a withdraw\n" << endl;
    }
}
void savings::savedeposit(float sdeposit)
{
    double below;
    cout << "Do you want to deposit money to your savings account?(1/0)\n1 is for yes, and 0 is for no\n";
    cin >> sdeposit;
    if (sdeposit == 1)
    {
        if (account < 25)
        {
            below = 25 - account;
            cout << "You're account is inactive. You must deposit at least" << below << " dollars for your account to be reactivated.\n";
            cout << "The current value of your account is " << account << " dollars.\n" << endl;
            cout << "Enter the amount you want to be deposited.\n" << endl;
            cin >> value;
            account = value - account;
            cout << "Your current account value is " << account << " dollars." << endl;
            
        }
        else
        {
            cout << "The current value of your account is " << account << " dollars.\n" << endl;
            cout << "Enter the amount you want to be deposited.\n" << endl;
            cin >> value;
            account = value + account;
            cout << "Your current account value is " << account << " dollars." << endl;
        }
    }
    else
    {
        cout << "You did not make a deposit.\n" << endl;
    }
}
void savings::saveproc(float sproc)
{
    int total;
    cout << "The bank charges a dollar every time you withdraw funds from your savings, if you've withdrawn more than 4 times.\n" << endl;
    if (SaveNumWithdraw > 4)
    {
        cout << "You have been charged $" << SaveNumWithdraw << ". \n";
        account = account - SaveNumWithdraw;
        cout << "Your current account value is " << account << " dollars\n" << endl;

        if (account < 25)
        {
            cout << "You're account is now inactive because your balance went below $25.\n";

        }
        else
        {
            cout << "You have not been charged a service charge.\n";
        }
    }
}

void mainBank::setDeposit(float deposit)
{
    cout << "Are you here to make a bank account deposit?(1/0)\n1 is for yes, and 0 is for no\n";
    cin >> deposit;
    if (deposit == 1)
    {
        cout << "The current value of your account is " << account << " dollars.\n" << endl;
        cout << "Enter the amount you want to be deposited\n" << endl;
        cin >> value;
        account = value + account;
        cout << "Your current account value is " << account << " dollars." << endl;
        NumDeposit = NumDeposit + 1;
    }
    else
    {
        cout << "You do not want to make a deposit\n" << endl;
    }
}
void mainBank::setWithdraw(float withdraw)
{
    cout << "Are you here to make a bank account withdraw?(1/0)\n1 is for yes, and 0 is for no\n" << endl;
    cin >> withdraw;
    if (withdraw == 1)
    {
        cout << "The current value of your account is " << account << " dollars" << endl;
        cout << "Enter the amount you want to be withdrawn.\n";
        cin >> value;
        account = account - value;
        cout << "Your current account value is " << account << " dollars" << endl;
        NumWithdraw = NumWithdraw + 1;
    }
    else
    {
        cout << "You do not want to make a withdraw\n" << endl;
    }
}
void mainBank::setMonthIntrest(float MonthIntrest)
{
    cout << "Are you here to calculate your monthly intrest for your bank acount?(1/0)\n1 is for yes, and 0 is for no\n" << endl;
    cin >> MonthIntrest;
    if (MonthIntrest == 1)
    {
        cout << "The current value of your account is " << account << " dollars" << endl;
        cout << "What is your monthly intrest rate\n";
        cin >> MonthIntrest;
        MonthIntrest = account * MonthIntrest;
        account = account + MonthIntrest;
        cout << "Current intrest generated by the monthly intrest rate is " << MonthIntrest << " dollars.\n total value of account is " << account << " dollars.\n";
        NumMonthIntrest = NumMonthIntrest + 1;
    }
    else
    {
        cout << "You do not want to make a to calculate your monthly intrest rate\n" << endl;
    }
}
void mainBank::setCharge(float charge)
{
    int total;
    cout << "The bank charges a dollar each time you use these services\n" << endl;
    total = NumDeposit + NumWithdraw + NumMonthIntrest;
    cout << "The bank will charge you " << total << "dollars" << endl;
    account = account - total;
    cout << "Your current account value is " << account << " dollars\n" << endl;
}
int main()
{
    int a;
    int i = 0;
    float values{};
    cout << "hello";
    mainBank Alpha;
    savings beta;
    checking_account gamma;
    while (i < 100)
    {
        i++;
        Alpha.setDeposit(values);
        Alpha.setWithdraw(values);
        Alpha.setMonthIntrest(values);
        Alpha.setCharge(values);
        beta.saveactivate(values);
        beta.savedeposit(values);
        beta.savewithdrawl(values);
        beta.saveproc(values);
        gamma.checkDeposit(values);
        gamma.checkWithdraw(values);
        gamma.checkwithdraw(values);
        gamma.checkCharge(values);
        gamma.checkMonthIntrest(values);
        cout << "Do you want to continue on?\n1 is for yes, and 0 is for no\n" << endl;
        cin >> a;
        if (a == 0)
        {
            break;
        }
    }

}
