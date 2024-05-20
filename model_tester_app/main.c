/*! ***************************************************************************
 *
 * \brief     Demo application
 * \file      main.c
 * \author    Hugo Arends
 * \date      July 2023
 *
 * \copyright 2023 HAN University of Applied Sciences. All Rights Reserved.
 *            \n\n
 *            Permission is hereby granted, free of charge, to any person
 *            obtaining a copy of this software and associated documentation
 *            files (the "Software"), to deal in the Software without
 *            restriction, including without limitation the rights to use,
 *            copy, modify, merge, publish, distribute, sublicense, and/or sell
 *            copies of the Software, and to permit persons to whom the
 *            Software is furnished to do so, subject to the following
 *            conditions:
 *            \n\n
 *            The above copyright notice and this permission notice shall be
 *            included in all copies or substantial portions of the Software.
 *            \n\n
 *            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *            EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 *            OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 *            NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 *            HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 *            WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 *            FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 *            OTHER DEALINGS IN THE SOFTWARE.
 *
 *****************************************************************************/
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>  // Header file for nanosleep

#include "features_calc.h"
#include "filters.h"
#include "normalizations.h"
#include "dtc/dtc_model.c"

#include "config.h"
#include "libserialport.h"

#define N_BUFFER (10)

char *port_name = "/dev/ttyACM0";

static volatile uint32_t ms = 0;
//static volatile uint32_t prev_ms = 0;

static uint32_t n = 0;
static float buffer_fp0_out[N_BUFFER];
static float buffer_fp1_out[N_BUFFER];
static float buffer_fp2_out[N_BUFFER];
static float buffer_fp3_out[N_BUFFER];
static float buffer_fp4_out[N_BUFFER];
static float buffer_fp5_out[N_BUFFER];
static float buffer_fp6_out[N_BUFFER];
static float buffer_fp7_out[N_BUFFER];
static float buffer_tof_out[N_BUFFER];

/* Helper function for error handling. */
int check(enum sp_return result)
{
        /* For this example we'll just exit on any error by calling abort(). */
        char *error_message;
        switch (result) {
        case SP_ERR_ARG:
                printf("Error: Invalid argument or port does not exist!.\n");
                abort();
        case SP_ERR_FAIL:
                error_message = sp_last_error_message();
                printf("Error: Failed: %s\n", error_message);
                sp_free_error_message(error_message);
                abort();
        case SP_ERR_SUPP:
                printf("Error: Not supported.\n");
                abort();
        case SP_ERR_MEM:
                printf("Error: Couldn't allocate memory.\n");
                abort();
        case SP_OK:
        default:
                return result;
        }
}

#include <string.h>
#include <libserialport.h>

char *read_line_from_serial(struct sp_port *port) {
    static char buffer[4096];  // Larger buffer to handle more data
    static int buffer_filled = 0;  // How much of the buffer is currently used
    char temp[1024];  // Temporary buffer for new data
    char *line_start = buffer;  // Pointer to the start of the current line in buffer

    // Read new data into temp buffer
    int bytes_read = sp_blocking_read(port, temp, sizeof(temp) - 1, 5);
    if (bytes_read > 0) {
        temp[bytes_read] = '\0';  // Null-terminate the new data

        // Check if there's space in buffer; if not, process or error handle
        if (buffer_filled + bytes_read >= sizeof(buffer)) {
            // fprintf(stderr, "Buffer overflow potential, data might be lost\n");
            buffer_filled = 0; // Reset buffer, might not be ideal depending on needs
            return NULL;
        }

        // Append new data to buffer
        memcpy(buffer + buffer_filled, temp, bytes_read);
        buffer_filled += bytes_read;
        buffer[buffer_filled] = '\0';  // Ensure buffer is null-terminated
    }

    // Search for newline in the buffer
    char *new_line = strchr(line_start, '\n');
    if (new_line) {
        *new_line = '\0';  // Replace newline with null-terminator
        char *complete_line = strdup(line_start);  // Duplicate the line to return
        buffer_filled -= (new_line + 1 - line_start);  // Adjust buffer usage
        memmove(buffer, new_line + 1, buffer_filled + 1);  // Shift remaining data
        return complete_line;
    }

    return NULL;  // No complete line read
}



int main(void)
{

    uint32_t ms1 = 0;
    uint32_t ms2 = 0;
    /* The ports we will use. */
    struct sp_port *port[2];
    check(sp_get_port_by_name(port_name, &port[0]));
    printf("Opening port.\n");
    check(sp_open(port[0], SP_MODE_READ_WRITE));
    printf("Setting port to 115200\n");
    check(sp_set_baudrate(port[0], 115200));
    char *data = "Hello!";
    int size = strlen(data);
    int result = check(sp_blocking_write(port[0], data, size, 1000));

    while(1)
    {
        char *line = read_line_from_serial(port[0]);
    if(line && strlen(line) < 62)
    {
        // Set initial timestamp
        ms1 = ms;
         printf("Received: %s\n", line);
         char *tokens[11];
         int i =0;
         char *token = strtok(line, ",");
            while (token != NULL && i < 11) {
                tokens[i++] = token;
                token = strtok(NULL, ",");
            }
        // printf("fp0: %s fp1: %s fp2: %s fp3: %s fp4: %s fp5: %s fp6: %s fp7: %s tof: %s\n", tokens[2],
        //                                                                                   tokens[3],
        //                                                                                   tokens[4],
        //                                                                                   tokens[5],
        //                                                                                   tokens[6],
        //                                                                                   tokens[7],
        //                                                                                   tokens[8],
        //                                                                                   tokens[9],
        //                                                                                   tokens[10]);
        // Buffer full?
        if(n >= (N_BUFFER-1))
        {
            // Remove first data item in the buffer and move all others one
            // position.
            memmove(&buffer_fp0_out[0], &buffer_fp0_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp1_out[0], &buffer_fp1_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp2_out[0], &buffer_fp2_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp3_out[0], &buffer_fp3_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp4_out[0], &buffer_fp4_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp5_out[0], &buffer_fp5_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp6_out[0], &buffer_fp6_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_fp7_out[0], &buffer_fp7_out[1], sizeof(float) * (N_BUFFER-1));
            memmove(&buffer_tof_out[0], &buffer_tof_out[1], sizeof(float) * (N_BUFFER-1));
        }
        if(i == 11) {
        // // Add data to the buffer
        buffer_fp0_out[n] = atof(tokens[2]);
        buffer_fp1_out[n] = atof(tokens[3]);
        buffer_fp2_out[n] = atof(tokens[4]);
        buffer_fp3_out[n] = atof(tokens[5]);
        buffer_fp4_out[n] = atof(tokens[6]);
        buffer_fp5_out[n] = atof(tokens[7]);
        buffer_fp6_out[n] = atof(tokens[8]);
        buffer_fp7_out[n] = atof(tokens[9]);
        buffer_tof_out[n] = atof(tokens[10]);
        n++;
        }

        // Buffer full?
        if(n >= N_BUFFER)
        {
            // Set counter at the end of the buffer
            n = N_BUFFER-1;


            // Calculate features by using feature functions
            //float y_out_var = variance(buffer_y_out, N_BUFFER);

            // Calculate label by using the generated Decision Tree
            // Classifier
            float fp5_var = variance(buffer_fp4_out, N_BUFFER);
            float fp3_var = variance(buffer_fp2_out, N_BUFFER);
            float tof_mean = mean(buffer_tof_out, N_BUFFER);
            float fp1_mean = mean(buffer_fp0_out, N_BUFFER);
            float fp2_mean = mean(buffer_fp1_out, N_BUFFER);
            float fp3_mean = mean(buffer_fp2_out, N_BUFFER);
            float fp4_mean = mean(buffer_fp3_out, N_BUFFER);
            float fp5_mean = mean(buffer_fp4_out, N_BUFFER);
            float fp6_mean = mean(buffer_fp5_out, N_BUFFER);
            float fp7_mean = mean(buffer_fp6_out, N_BUFFER);
            float fp8_mean = mean(buffer_fp7_out, N_BUFFER);

            dtc_t label = dtc(fp5_var, buffer_fp1_out[n], fp4_mean, buffer_fp7_out[n], buffer_fp5_out[n], tof_mean, fp7_mean, buffer_fp6_out[n], fp8_mean, fp6_mean, buffer_fp1_out[n], fp1_mean, fp3_mean, fp5_mean, fp3_var);
            
            char *label_str = "";

            //Use the calculated label for further processing
            if(label == undetermined)
            {
                    label_str = "undetermined";
            }
            else if(label == suboptimal_high_finger_placement)
            {
                    label_str = "suboptimal_high_finger_placement";
            }
            else if(label == suboptimal_left_centered)
            {
                    label_str = "suboptimal_left_centered";
            }
            else if(label == suboptimal_too_much_force)
            {
                    label_str = "suboptimal_too_much_force";
            }
            else if(label == optimal)
            {
                    label_str = "optimal";
            }
            else if(label == optimal)
            {
                    label_str = "optimal";
            }
            // Set final timestamp
            ms2 = ms;
            
            // Print duration and label
            printf("%d,%d,%s\n",
                ms1,
                ms2,
                label_str);
        }
    }
        
    }
    check(sp_close(port[0]));
    sp_free_port(port[0]);
}

