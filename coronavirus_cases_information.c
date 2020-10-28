// program to get no of coronavirus cases in a country
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define CORONAVIRUSCASES_INFORMATION_OF_ALL_COUNTRIES_FILE "coronavirus_cases_of_all_countries.dat"
#define SEARCH_DELIMITERS "{,:\""
void display_number_of_coronavirus_cases(char*, char*);
void data_of_coronavirus_cases_around_the_world(char*);
char* get_number_of_coronavirus_cases_in_a_country(char*);

int main(int argc, char *argv[])
{
	char country_name[20];
	if(argv[1] == NULL)
	{
		printf("Enter a country name: ");
		scanf("%s", country_name);
	}
	else
	{
		strcpy(country_name, argv[1]);
	}
	data_of_coronavirus_cases_around_the_world(country_name);
	return 0;
}

void data_of_coronavirus_cases_around_the_world(char *country_name)
{
	char command[100];
	sprintf(command, "curl \"https://api.covid19api.com/summary\" > %s -s", CORONAVIRUSCASES_INFORMATION_OF_ALL_COUNTRIES_FILE);
	system(command);
	char *total_coronavirus_cases = get_number_of_coronavirus_cases_in_a_country(country_name);
	display_number_of_coronavirus_cases(total_coronavirus_cases, country_name);
}

char* get_number_of_coronavirus_cases_in_a_country(char *location)
{
	FILE *fp_coronaviruscases_information;
	fp_coronaviruscases_information = fopen("coronaviruscases.dat", "r");
	char world_coronaviruscases_information[50000];
	char *total_cases;
	fread(world_coronaviruscases_information, sizeof(world_coronaviruscases_information), 1, fp_coronaviruscases_information);
	char *ptr_token;
	ptr_token = strtok(world_coronaviruscases_information, SEARCH_DELIMITERS);
	while(ptr_token != NULL)
	{
		if(strcmp(ptr_token, location) == 0)
		{
			while(ptr_token != NULL)
			{
				int is_totalcases_found = 0;
				if(strcmp(ptr_token, "TotalConfirmed") == 0)
				{
					is_totalcases_found = 1;
				}
				ptr_token = strtok(NULL, SEARCH_DELIMITERS);
				if(is_totalcases_found == 1)
				{
					total_cases = ptr_token;
					break;
				}
			}
		}
		ptr_token = strtok(NULL, SEARCH_DELIMITERS);
	}
	fclose(fp_coronaviruscases_information);
	return total_cases;
}

void display_number_of_coronavirus_cases(char *total_cases, char* country)
{
	printf("The total coronavirus cases in %s is %s.", country, total_cases);
}