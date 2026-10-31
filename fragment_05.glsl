#version 330

uniform vec2 iResolution;
uniform float u_scale;
out vec4 frag_color;
// aspect ratio
const float _a = 16.0/9.0;

void main(){
    // Normalize
    vec2 uv = u_scale *  gl_FragCoord.xy / vec2(iResolution.x / _a, iResolution.y) * 2;
    uv = uv - vec2(_a , 1);

    frag_color = vec4(uv, 0.0, 1.0);
}
