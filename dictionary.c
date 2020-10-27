// Get the meaning and pronunciation of a word in dictionary
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define INFORMATION_OF_WORD "information_of_word.dat"
#define SEARCH_DELIMITERS "{,\""
void display_definition(char*, char*);
char* get_definition_of_word();
void play_audio();
void information_of_the_word();

int main()
{
	information_of_the_word();
}

void information_of_the_word()
{
	char given_word_to_find_meaning[20];
	char command[100];
	char *meaning_of_the_word;
	printf("Enter a word to find its meaning and pronunciation: ");
	scanf("%s", given_word_to_find_meaning);
	sprintf(command, "curl \"https://api.dictionaryapi.dev/api/v2/entries/en/%s\" -o %s -s", given_word_to_find_meaning, INFORMATION_OF_WORD);
	system(command);
	meaning_of_the_word = get_definition_of_word();
	display_definition(meaning_of_the_word, given_word_to_find_meaning);
	play_audio();
}

void play_audio()
{
	FILE *fp_audio_of_word;
	char data_from_file[1000];
	fp_audio_of_word = fopen(INFORMATION_OF_WORD, "r");
	fread(data_from_file, sizeof(data_from_file), 1, fp_audio_of_word);
	char command_to_play_audio[100];
	char *ptr_token_of_the_string;
	ptr_token_of_the_string = strtok(data_from_file, SEARCH_DELIMITERS);
	while(ptr_token_of_the_string != NULL)
	{
		int audio_found = 0;
		if(strcmp(ptr_token_of_the_string, "audio") == 0)
		{
			audio_found = 1;
		}
		ptr_token_of_the_string = strtok(NULL, SEARCH_DELIMITERS);
		if(audio_found == 1)
		{
			ptr_token_of_the_string = strtok(NULL, SEARCH_DELIMITERS);
			printf("%s", ptr_token_of_the_string);
			sprintf(command_to_play_audio ,"vlc -I null --play-and-exit  \"ptr_token_of_the_string\"");
			system(command_to_play_audio);
		}
	}
	fclose(fp_audio_of_word);
}

char* get_definition_of_word()
{
	FILE *fp_data_of_word;
	fp_data_of_word = fopen(INFORMATION_OF_WORD, "r");
	char data_from_file[1000];
	fread(data_from_file, sizeof(data_from_file), 1, fp_data_of_word);
	char *ptr_token_of_the_string;
	char *meaning_of_word;
	ptr_token_of_the_string = strtok(data_from_file, SEARCH_DELIMITERS);
	while(ptr_token_of_the_string != NULL)
	{
		int meaning_found = 0;
		if(strcmp(ptr_token_of_the_string, "definition") == 0)
		{
			meaning_found = 1;
		}
		ptr_token_of_the_string = strtok(NULL, SEARCH_DELIMITERS);
		if(meaning_found == 1)
		{
			ptr_token_of_the_string = strtok(NULL, SEARCH_DELIMITERS);
			meaning_of_word = ptr_token_of_the_string;
		}	
	}
	fclose(fp_data_of_word);
	return meaning_of_word; 
}

void display_definition(char *definition_of_word, char* given_word)
{
	printf("Meaning of %s: %s\n", given_word, definition_of_word);
}

