#ifndef DEBUG_LOGGING_H
#define DEBUG_LOGGING_H

#include <stdio.h>
#include <stdarg.h>

#ifdef __cplusplus
extern "C" {
#endif

// Debug logging levels
typedef enum {
    DEBUG_LOG_LEVEL_NONE = 0,
    DEBUG_LOG_LEVEL_ERROR = 1,
    DEBUG_LOG_LEVEL_WARN = 2,
    DEBUG_LOG_LEVEL_INFO = 3,
    DEBUG_LOG_LEVEL_DEBUG = 4
} DebugLogLevel;

// Module identifiers for logging
typedef enum {
    DEBUG_LOG_MODULE_SIMPLE_CALC = 0,
    DEBUG_LOG_MODULE_PROG_CALC = 1,
    DEBUG_LOG_MODULE_CALC_CHECK = 2,
    DEBUG_LOG_MODULE_GENERAL = 3
} DebugLogModule;

// Core logging functions
void debugLog_init(DebugLogLevel level);
void debugLog_setLevel(DebugLogLevel level);
DebugLogLevel debugLog_getLevel(void);

void debugLog_print(DebugLogModule module, DebugLogLevel level, const char* format, ...);
void debugLog_printRaw(const char* format, ...);

// Convenience macros for different modules
#define DEBUG_LOG_SIMPLE_CALC(fmt, ...) \
    debugLog_print(DEBUG_LOG_MODULE_SIMPLE_CALC, DEBUG_LOG_LEVEL_DEBUG, fmt, ##__VA_ARGS__)

#define DEBUG_LOG_PROG_CALC(fmt, ...) \
    debugLog_print(DEBUG_LOG_MODULE_PROG_CALC, DEBUG_LOG_LEVEL_DEBUG, fmt, ##__VA_ARGS__)

#define DEBUG_LOG_CALC_CHECK(fmt, ...) \
    debugLog_print(DEBUG_LOG_MODULE_CALC_CHECK, DEBUG_LOG_LEVEL_DEBUG, fmt, ##__VA_ARGS__)

#define DEBUG_LOG_ERROR(module, fmt, ...) \
    debugLog_print(module, DEBUG_LOG_LEVEL_ERROR, fmt, ##__VA_ARGS__)

#define DEBUG_LOG_WARN(module, fmt, ...) \
    debugLog_print(module, DEBUG_LOG_LEVEL_WARN, fmt, ##__VA_ARGS__)

#define DEBUG_LOG_INFO(module, fmt, ...) \
    debugLog_print(module, DEBUG_LOG_LEVEL_INFO, fmt, ##__VA_ARGS__)

#ifdef __cplusplus
}
#endif

#endif // DEBUG_LOGGING_H
