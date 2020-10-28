// program to get no of coronavirus cases in a country
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define CORONAVIRUSCASES_INFORMATION_OF_ALL_COUNTRIES_FILE "coronavirus_cases_of_all_countries.dat"
#define SEARCH_DELIMITERS "{,:\""

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
	char command[100];
	char *ptr_token;
	char world_coronaviruscases_information[50000];
	sprintf(command, "curl \"https://api.covid19api.com/summary\" > %s -s", CORONAVIRUSCASES_INFORMATION_OF_ALL_COUNTRIES_FILE);
	system(command);
	FILE *fp_coronaviruscases_information;
	fp_coronaviruscases_information = fopen("coronaviruscases.dat", "r");
	fread(world_coronaviruscases_information, sizeof(world_coronaviruscases_information), 1, fp_coronaviruscases_information);
	ptr_token = strtok(world_coronaviruscases_information, SEARCH_DELIMITERS);
	while(ptr_token != NULL)
	{
		if(strcmp(ptr_token, country_name) == 0)
		{
			while(ptr_token != NULL)
			{
				int is_total_cases_found = 0;
				if(strcmp(ptr_token, "TotalConfirmed") == 0)
				{
					is_total_cases_found = 1;
				}
				ptr_token = strtok(NULL, SEARCH_DELIMITERS);
				if(is_total_cases_found == 1)
				{
					printf("The total coronavirus cases in %s is %s.", country_name, ptr_token);
					break;
				}
			}
		}
		ptr_token = strtok(NULL, SEARCH_DELIMITERS);
	}
	fclose(fp_coronaviruscases_information);
}