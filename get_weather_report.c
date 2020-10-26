// Get weather of a given city
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SEARCH_DELEMITERS "{:,["
#define WEATHER_REPORT_FILE "weather_report.dat"
void display_temperature(char* token);
void is_pointer_null(FILE*);
void load_weather_report();
char* get_temperature(char);

int main()
{
	display_temperature();
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
	ptr_token_of_string = strtok(weather_report, SEARCH);
	while(ptr_token_of_string != NULL)
	{
		int temperature_found = 0;
		if(strcmp(ptr_token_of_string, "\"temp\"") == 0)
		{
			temperature_found = 1;
		}
		ptr_token_of_string = strtok(NULL, SEARCH);
		if(temperature_found == 1)
		{
			temperature_in_weather_report_file = ptr_token_of_string;
		}
	}
	fclose(fp_weather_report);
	return temperature_in_weather_report_file;
}

void display_temperature()
{
	printf("Enter a city name: ");
	char city[20];
	scanf("%s", city);
	load_weather_report(city, WEATHER_REPORT_FILE);
	char *temperture = get_temperature(WEATHER_REPORT_FILE);
	printf("The temperature in %s is %s.",city, temperature);
}

void load_weather_report(char *city_name, char *file_name)
{
	char command[200];
	sprintf(command, "curl \"http://api.openweathermap.org/data/2.5/find?q=%s&appid=7a9f30882737a25fea0fcf2974889d24&units=metric\" > %s -s", city_name, file_name);
	system(command);
}

void is_pointer_null(FILE *temp_file)
{
	if(temp_file == NULL)
	{
		printf("File does not exist or unable to open the file.");
	}
}