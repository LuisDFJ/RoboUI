#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNorm;

uniform mat4 transform;
out vec3 Norm;
out vec3 FragPos;

void main()
{
    gl_Position = transform * vec4( aPos, 1.0f );
    FragPos     = vec3( transform * vec4( aPos, 1.0f ) );
    Norm        = aNorm;
}