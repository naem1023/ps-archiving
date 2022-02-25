#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct Version {
    uint8_t major;
    uint8_t minor;
    uint16_t patch;
} Version;

typedef struct Application {
    Version version;
    char*   name;
} Application;

/// TODO_1: Implement code.
///  It sets the version and the name to 'Application* out_app'.
///  'char* name' in 'struct Application' must be allocated and be copied from input 'const char* name'.
///  [Input]
///    - uint32_t version : 0x{patch:2bytes}{minor:1bytes}{major:1bytes}
///    - const char* name : string.
///  [Output]
///    - Application* out_app
void configure_app(Application* out_app, uint32_t version, const char* name)
{
    uint16_t patch = version >> 16;
    uint8_t minor = (version >> 8) & 0x00F;
    uint8_t major = version & 0x000F;
    
    out_app->version.patch = patch;
    out_app->version.minor = minor;
    out_app->version.major = major;
    out_app->name = strncpy(out_app->name, name, sizeof(name) / sizeof(char));
    
    // *(uint32_t*)&app->version = version;
    // out_app->name = strncpy(out_app->name, name, strlen(name));
}

/// TODO_2: Implement code.
///  It returns TRUE(0) or FALSE(-1) after comparing app1 and app2.
///  [Input]
///    - Application* app1 : compare A
///    - Application* app2 : compare B
///  [Return]
///    - Return TRUE condition: same version and same name.
int is_same_app(Application* app1, Application* app2)
{
    if (app1->version.patch == app2->version.patch && 
        app1->version.major == app2->version.major &&
        app1->version.minor == app2->version.minor &&
        strcmp(app1->name, app2->name) == 0
        ) {
        return 0;   
    }
    else {
        return -1;
    }
}

int main() {
    Application app1, app2;
    configure_app(&app1, 0x00040201, "app1");
    configure_app(&app2, 0x01231003, "app2");

    int ret = is_same_app(&app1, &app2);
    printf("Name(%s) Version(%d.%d.%d)\n", app1.name, app1.version.major, app1.version.minor, app1.version.patch);
    printf("Name(%s) Version(%d.%d.%d)\n", app2.name, app2.version.major, app2.version.minor, app2.version.patch);
    printf("%s and %s are %s\n", app1.name, app2.name, ret == 0 ? "same" : "different");

    return 0;
}
