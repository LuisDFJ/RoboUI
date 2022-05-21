#version 330 core

uniform vec3 uColor;
out vec4 FragColor;
in vec3 Norm;
in vec3 FragPos;

void main()
{
    
    vec3 lightPos   = vec3( 10.0, 10.0, -10.0 );
    vec3 lightDir   = normalize( lightPos - FragPos );
    float diff      = max( dot( Norm, lightDir ), 0.0 );
    float ambient   = 0.4;
    vec3 color      = ( diff + ambient ) * uColor;
    //vec3 color      = ( diff + ambient ) * vec3( 0.9, 0.9, 0.9 );
    FragColor = vec4( color, 1.0f );
}