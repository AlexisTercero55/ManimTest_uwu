#version 330

out vec4 frag_color;
uniform float r;
uniform float g;
uniform float b;

void main(){
    frag_color = vec4(r, g, b, 1.0);
}
