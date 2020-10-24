//framework 
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define LENGTH_OF_FIELDNAME 20
#define LENGTH_OF_FIELD_DATA 20
#define LENGTH_OF_MENU 500
#define LENGTH_OF_UPDATABLE_FIELD_POSITION 5
#define FIELD_DATA "data.dat"
#define FIELD_CONFIG_FILE "fields.cfg"
#define MENU_CONFIG_FILE "menu.cfg"
#define UPDATABLE_CONFIG_FILE "updatable_fields_position.cfg"

void add_record();
int get_count_of_updatable_fields_position();
void print_not_found();
void delete_record();
void update_record();
void is_pointer_null(FILE*);
void initialize_global_variables();
int get_count_of_field_names();
void load_updatable_fields_position_into_array();
void print_menu();
void load_field_names_into_array();
void print_all_records();

FILE *fp_fields;
FILE *fp_updatable_fields_position;
int count_of_field_names;
int count_of_updatable_fields_position;
char **ptr_field_names;
int *ptr_updatable_fields_position;

int main()
{
	initialize_global_variables();
	print_menu();
	return 0;
}

void initialize_global_variables()
{
	fp_fields = fopen(FIELD_CONFIG_FILE, "r");
	count_of_field_names = get_count_of_field_names();
	rewind(fp_fields);
	load_field_names_into_array();
	fclose(fp_fields);
	fp_updatable_fields_position = fopen(UPDATABLE_CONFIG_FILE, "r");
	count_of_updatable_fields_position = get_count_of_updatable_fields_position();
	rewind(fp_updatable_fields_position);
	load_updatable_fields_position_into_array();
	fclose(fp_updatable_fields_position);
}

int get_count_of_field_names()
{
	int temp_counter_of_fields = 0;
	char field_name[LENGTH_OF_FIELDNAME];
	while(fgets(field_name, sizeof(field_name), fp_fields) != NULL)
	{
		temp_counter_of_fields++;
	}
	return temp_counter_of_fields;
}

void load_field_names_into_array()
{
	char field_name[LENGTH_OF_FIELDNAME];
	ptr_field_names = malloc(count_of_field_names * sizeof(char*));
	for(int row_counter = 0; row_counter < count_of_field_names; row_counter++)
	{
		ptr_field_names[row_counter] = malloc(LENGTH_OF_FIELDNAME);
		fgets(field_name, sizeof(field_name), fp_fields);
		field_name[strlen(field_name) - 1 ] = '\0';
		strcpy(ptr_field_names[row_counter], field_name);
	}
}

void load_updatable_fields_position_into_array()
{
	char updatable_field_position[LENGTH_OF_UPDATABLE_FIELD_POSITION];
	ptr_updatable_fields_position = malloc(count_of_updatable_fields_position * sizeof(int));
	for(int row_counter = 0; row_counter < count_of_updatable_fields_position; row_counter++)
	{
		fgets(updatable_field_position, sizeof(updatable_field_position), fp_updatable_fields_position);
		updatable_field_position[strlen(updatable_field_position) - 1] = '\0';
		ptr_updatable_fields_position[row_counter] = atoi(updatable_field_position);
	}
}


void is_pointer_null(FILE *fp_temp_file)
{
	if(fp_temp_file == NULL)
	{
		printf("FILE DOES NOT EXIST OR UNABLE TO OPEN THE FILE.");
		exit(0);
	}
}

int get_count_of_updatable_fields_position()
{
	int temp_counter_of_fields_position = 0;
	char updatable_field_position[LENGTH_OF_UPDATABLE_FIELD_POSITION];
	while(fgets(updatable_field_position, sizeof(updatable_field_position), fp_updatable_fields_position) != NULL)
	{
		temp_counter_of_fields_position++;
	}
	return temp_counter_of_fields_position;
}

void print_menu()
{
	FILE *fp_menu = fopen(MENU_CONFIG_FILE, "r");
	is_pointer_null(fp_menu);
	char menu[LENGTH_OF_MENU];
	fread(menu, sizeof(menu), 1, fp_menu);
	fclose(fp_menu);
	while(1)
	{
		printf("%s", menu);
		printf("Enter a number: ");
		int user_choice;
		scanf("%d", &user_choice);
		switch(user_choice)
		{
			case 1: add_record();
					break;
			case 2: print_all_records();
					break;
			case 3: update_record();
					break;
			case 4: delete_record();
					break;
			case 5: exit(0);
			default: printf("ENTER A VALID NUMBER.");
		}
	}
}

void add_record()
{
	FILE *fp_data_of_fields;
	fp_data_of_fields = fopen(FIELD_DATA, "a");
	is_pointer_null(fp_data_of_fields);
	char field_value[LENGTH_OF_FIELD_DATA];
	char record_status = 'A';
	fwrite(&record_status, sizeof(record_status), 1, fp_data_of_fields);
	for(int row_counter = 0; row_counter < count_of_field_names; row_counter++)
	{
		printf("Enter %s: ", ptr_field_names[row_counter]);
		scanf("%s", field_value);
		fwrite(field_value, sizeof(field_value), 1, fp_data_of_fields);
	}
	fclose(fp_data_of_fields);
}

void print_all_records()
{
	FILE *fp_data_of_fields;
	fp_data_of_fields = fopen(FIELD_DATA, "r");
	is_pointer_null(fp_data_of_fields);
	char field_value[LENGTH_OF_FIELD_DATA];
	char record_status;
	char record[count_of_field_names * LENGTH_OF_FIELD_DATA];
	while(fread(&record_status, sizeof(record_status), 1, fp_data_of_fields))
	{
		if(record_status == 'A')
		{
			for(int row_counter = 0; row_counter < count_of_field_names; row_counter++)
			{
				fread(field_value, sizeof(field_value), 1, fp_data_of_fields);
				printf("%s: %s\n", ptr_field_names[row_counter], field_value);
			}
		}
		else
		{
			fseek(fp_data_of_fields, sizeof(record), SEEK_CUR);
		}
	}
	fclose(fp_data_of_fields);
}

void update_record()
{
	FILE *fp_data_of_fields;
	fp_data_of_fields = fopen(FIELD_DATA, "r+");
	is_pointer_null(fp_data_of_fields);
	FILE *fp_updatable_fields_position;
	fp_updatable_fields_position = fopen(UPDATABLE_CONFIG_FILE, "r");
	is_pointer_null(fp_updatable_fields_position);
	char field_value[LENGTH_OF_FIELD_DATA];
	int record_found = 0;
	char record[count_of_field_names * LENGTH_OF_FIELD_DATA];
	char given_data_to_update_field_value[LENGTH_OF_FIELD_DATA];
	printf("Enter %s: ", ptr_field_names[0]);
	scanf("%s", given_data_to_update_field_value);
	char record_status;
	char updated_data_of_field[LENGTH_OF_FIELD_DATA];
	while(fread(&record_status, sizeof(record_status), 1, fp_data_of_fields))
	{
		if(record_status == 'A')
		{
			fread(field_value, sizeof(field_value), 1, fp_data_of_fields);
			if(strcmp(field_value, given_data_to_update_field_value) == 0)
			{
				record_found = 1;
				for(int row_counter = 0; row_counter < count_of_updatable_fields_position; row_counter++)
				{
					printf("%d. Update %s\n", row_counter + 1, ptr_field_names[ptr_updatable_fields_position[row_counter] - 1]);
				}
				int user_choice;
				printf("Enter a number: ");
				scanf("%d", &user_choice);
				printf("Enter new %s: ", ptr_field_names[ptr_updatable_fields_position[user_choice - 1] - 1]);
				scanf("%s", updated_data_of_field);
				fseek(fp_data_of_fields, ((ptr_updatable_fields_position[user_choice - 1]) - 2) * sizeof(field_value), SEEK_CUR);
				fwrite(updated_data_of_field, sizeof(updated_data_of_field), 1, fp_data_of_fields);
				printf("%s is successfully updated.\n", ptr_field_names[ptr_updatable_fields_position[user_choice - 1] - 1]);
				break;
			}
			else
			{
				fseek(fp_data_of_fields, (count_of_field_names -1) * sizeof(field_value), SEEK_CUR);
			}
		}
		else
		{
			fseek(fp_data_of_fields, sizeof(record), SEEK_CUR);
		}		 
	}
	if(record_found == 0)
	{
		print_not_found();
	}
	fclose(fp_data_of_fields);
	fclose(fp_updatable_fields_position);
}

void delete_record()
{
	FILE *fp_data_of_fields;
	fp_data_of_fields = fopen(FIELD_DATA, "r+");
	is_pointer_null(fp_data_of_fields);
	char data_of_field[LENGTH_OF_FIELD_DATA];
	char given_field_value_to_delete_record[LENGTH_OF_FIELD_DATA];
	printf("Enter %s: ", ptr_field_names[0]);
	fflush(stdin);
	scanf("%s", given_field_value_to_delete_record);
	char record_status;
	int record_found = 0;
	char record[count_of_field_names * LENGTH_OF_FIELD_DATA];
	while(fread(&record_status, sizeof(record_status), 1, fp_data_of_fields))
	{
		if(record_status == 'A')
		{
			fread(data_of_field, sizeof(data_of_field), 1, fp_data_of_fields);
			if(strcmp(data_of_field, given_field_value_to_delete_record) == 0)
			{
				fseek(fp_data_of_fields, -1 * sizeof(data_of_field) - 1, SEEK_CUR);
				char change_status = 'I';
				fwrite(&change_status, sizeof(change_status), 1, fp_data_of_fields);
				printf("Record is deleted.\n");
				record_found = 1;
				break;
			}
			else
			{
				fseek(fp_data_of_fields, (count_of_field_names - 1) * sizeof(data_of_field), SEEK_CUR);
			}
		}
		else
		{
			fseek(fp_data_of_fields, sizeof(record), SEEK_CUR);
		}
	}
	if(record_found == 0)
	{
		print_not_found();
	}
	fclose(fp_data_of_fields);	
}

void print_not_found()
{
	printf("Record is not found.\n");
}