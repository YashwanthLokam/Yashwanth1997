// create a structure and preform operations on it.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define NAME_LENGTH 30
#define NUMBER_LENGTH 12
#define BALANCE_LENGTH 10
#define FILE_NAME "Bank_account7.txt"
#define TEMP_FILE "Tempfile2.txt"
void is_updated(int);
void is_record_not_found(int);
void is_successfull(int);
void is_pointer_null(FILE*);
void view_accounts();
void update_an_account();
void show_menu();
void create_an_account();
void delete_an_account();

struct bank_account
{
	char account_holder[NAME_LENGTH];
	char account_number[NUMBER_LENGTH];
	char balance[BALANCE_LENGTH];
	char status;
};

int main()
{
	while(1)
	{
		show_menu();
	}
	return 0;
}

void show_menu()
{
	printf("1. Create an account\n2. View accounts\n3. Update an account\n4. Delete an account\n5. Exit\n");
	printf("Enter a number: ");
	int choice;
	scanf("%d", &choice);
	switch(choice)
	{
		case 1: create_an_account();
				break;
		case 2: view_accounts();
				break;
		case 3: update_an_account();
				break;
		case 4: delete_an_account();
				break;
		case 5: exit(0);
		default: printf("Enter a valid number");
	}
}

void is_pointer_null(FILE *fp_bank_account1)
{
	if(fp_bank_account1 == NULL)
	{
		printf("File does not exist or unable to open the file.");
		exit(0);
	}
}

void create_an_account()
{
	struct bank_account record;
	FILE *fp_bank_account;
	fp_bank_account = fopen(FILE_NAME, "a");
	is_pointer_null(fp_bank_account);
	printf("Enter the customer name: ");
	fflush(stdin);
	scanf("%s", record.account_holder);
	printf("Enter balance: ");
	scanf("%s", record.balance);
	printf("Enter account number: ");
	scanf("%s", record.account_number);
	int Count_of_records_stored = fwrite(&record, sizeof(record), 1, fp_bank_account);
	if(Count_of_records_stored == 1)
	{
		is_successfull(1);
	}
	else
	{
		is_record_not_found(1);
	}
	fclose(fp_bank_account);
}

void view_accounts()
{
	struct bank_account record;
	FILE *fp_bank_account;
	fp_bank_account = fopen(FILE_NAME, "r");
	is_pointer_null(fp_bank_account);
	fflush(stdin);
	while(fread(&record, sizeof(record), 1, fp_bank_account))
	{
		printf("Account holder: %s\nAccount number: %s\nBalance: %s\n", record.account_holder, record.account_number, record.balance);
	}
	fclose(fp_bank_account);
}

void update_an_account()
{
	struct bank_account record;
	FILE *fp_bank_account;
	fp_bank_account = fopen(FILE_NAME, "r+");
	fflush(stdin);
	int is_account_number_present = 0;
	is_pointer_null(fp_bank_account);
	char account_number_to_update_balance[NUMBER_LENGTH];
	printf("Enter the account number to update: ");
	scanf("%s", account_number_to_update_balance);
	while(fread(&record, sizeof(record), 1, fp_bank_account))
	{
		if(strcmp(record.account_number, account_number_to_update_balance) == 0) 
		{
			int choice1;
			printf("1. Update account name\n2. Update balance\n");
			scanf("%d", &choice1);
			is_account_number_present = 1;
			if(choice1 == 1)
			{
				printf("Enter new account name: ");
				char new_account_holder[NAME_LENGTH];
				scanf("%s", new_account_holder);
				fseek(fp_bank_account, -1 * sizeof(record), SEEK_CUR);
				fwrite(new_account_holder, NAME_LENGTH, 1, fp_bank_account);
				is_updated(1);
				break;
			}
			if(choice1 == 2)
			{
				printf("Enter new balance: ");
				char new_balance[BALANCE_LENGTH];
				scanf("%s", new_balance);
				fseek(fp_bank_account, -1 * BALANCE_LENGTH, SEEK_CUR);
				fwrite(new_balance, BALANCE_LENGTH, 1, fp_bank_account);
				is_updated(2);
				break;
			}
		}
	}
	fflush(stdin);
	if(is_account_number_present == 0)
	{
		is_record_not_found(2);
	}
	fclose(fp_bank_account);
}

void delete_an_account()
{
	struct bank_account record;
	FILE *fp_bank_account;
	fp_bank_account = fopen(FILE_NAME, "r");
	is_pointer_null(fp_bank_account);
	FILE *fp_temp_bank_account;
	fp_temp_bank_account = fopen(TEMP_FILE, "w");
	is_pointer_null(fp_bank_account);
	fflush(stdin);
	int is_record_present = 0;
	char account_number_to_be_deleted[NUMBER_LENGTH];
	printf("Enter the account number: ");
	scanf("%s", &account_number_to_be_deleted);
	while(fread(&record, sizeof(record), 1, fp_bank_account))
	{
		if(strcmp(record.account_number, account_number_to_be_deleted) == 0)
		{
			is_record_present = 1;
		}
		else
		{
			fwrite(&record, sizeof(record), 1, fp_temp_bank_account);
		}
	}
	if(is_record_present == 1)
	{
		is_successfull(2);
	}
	else
	{
		is_record_not_found(2);
	}
	fclose(fp_bank_account);
	fclose(fp_temp_bank_account);
	remove(FILE_NAME);
	rename(TEMP_FILE, FILE_NAME);
}

void is_record_not_found(int value)
{
	printf("Record is%sin the file.\n", value == 1 ? " not stored " : " not found ");
}

void is_successfull(int value)
{
	printf("Record is successfully%sfile.\n", value == 1 ? " stored in the " : " deleted from ");
}

void is_updated(int value)
{
	printf("%sis updated.\n", value == 1 ? " Account number" : " Balance ");
}