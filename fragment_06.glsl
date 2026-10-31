#version 330

uniform vec2 iResolution;
uniform float iTime;
uniform float u_scale;
// aspect ratio
const float _a = 16.0/9.0;

out vec4 frag_color;

void main(){
    // Normalize
    vec2 uv = u_scale *  gl_FragCoord.xy / vec2(iResolution.x / _a, iResolution.y) * 2;
    uv = uv - vec2(_a , 1);

    float d = length(uv);
    vec3 col = vec3(1.0, 2.0, 3.0);

    d = sin(d*8. + iTime)/8.;
    d = abs(d);

    d = 0.02 / d;

    col *= d;

    frag_color = vec4(col, 1.0);
}
