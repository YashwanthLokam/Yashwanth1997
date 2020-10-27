// Get weather of a given city
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SEARCH_DELIMITERS "{:,["
#define WEATHER_REPORT_FILE "weather_report.dat"
void display_temperature(char*);
void is_pointer_null(FILE*);
void load_weather_report(char*, char*);
char* get_temperature(char*);

int main(int argc, char* argv[])
{
	char city[20];
	if(argv[1] == NULL)
	{
		printf("Enter a city name: ");
		scanf("%s", city);
	}
	else
	{
		strcpy(city, argv[1]);
	}
	display_temperature(city);
}

char* get_temperature(char *file_name)
{
	char *ptr_token_of_string;
	char *temperature_in_weather_report_file;
	char weather_report[1000];
	FILE *fp_weather_report;
	fp_weather_report = fopen(file_name, "r");
	is_pointer_null(fp_weather_report);
	fread(weather_report, sizeof(weather_report), 1, fp_weather_report);
	ptr_token_of_string = strtok(weather_report, SEARCH_DELIMITERS);
	while(ptr_token_of_string != NULL)
	{
		int temperature_found = 0;
		if(strcmp(ptr_token_of_string, "\"temp\"") == 0)
		{
			temperature_found = 1;
		}
		ptr_token_of_string = strtok(NULL, SEARCH_DELIMITERS);
		if(temperature_found == 1)
		{
			temperature_in_weather_report_file = ptr_token_of_string;
		}
	}
	fclose(fp_weather_report);
	return temperature_in_weather_report_file;
}

void display_temperature(char *location)
{
	char degree_symbol = 248;
	load_weather_report(location, WEATHER_REPORT_FILE);
	char *temperature = get_temperature(WEATHER_REPORT_FILE);
	printf("The temperature in %s is %s%cC", location, temperature, degree_symbol);
}

void load_weather_report(char *city_name, char *file_name)
{
	char command[300];
	sprintf(command, "curl \"http://api.openweathermap.org/data/2.5/find?q=%s&appid=7a9f30882737a25fea0fcf2974889d24&units=metric\" > %s -s", city_name, file_name);
	system(command);
}

void is_pointer_null(FILE *temp_file)
{
	if(temp_file == NULL)
	{
		printf("File does not exist or unable to open the file.");
		exit(0);
	}
}