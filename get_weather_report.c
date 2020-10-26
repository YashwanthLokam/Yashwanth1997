// Get weather of a given city
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SEARCH "{:,["
void is_pointer_null(FILE*);

int main()
{
	printf("Enter a city name: ");
	char city[20];
	char command[200];
	char *token;
	char weather_report[1000];
	scanf("%s", city);
	sprintf(command, "curl \"http://api.openweathermap.org/data/2.5/find?q=%s&appid=7a9f30882737a25fea0fcf2974889d24&units=metric\" > weather_report.dat", city);
	system(command);
	FILE *fp_weather_report;
	fp_weather_report = fopen("weather_report.dat", "r");
	is_pointer_null(fp_weather_report);
	fread(weather_report, sizeof(weather_report), 1, fp_weather_report);
	token = strtok(weather_report, SEARCH);
	while(token != NULL)
	{
		if(strcmp(token, "\"temp\"") == 0)
		{
			break;
		}
		token = strtok(NULL, SEARCH);
	}
	printf("The temperature of %s is %s.", city, strtok(NULL, SEARCH));
}

void is_pointer_null(FILE *temp_file)
{
	if(temp_file == NULL)
	{
		printf("File does not exist or unable to open the file.");
	}
}