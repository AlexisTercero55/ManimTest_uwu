#version 330

out vec4 frag_color;
uniform vec2 iResolution;

void main(){
    vec2 uv = gl_FragCoord.xy / iResolution.xy;
    // Use gl_FragCoord.xy and not gl_FragCoord
    // because gl_FragCoord is a 3d vector, not
    // 2d like in ShaderToy
    frag_color = vec4(uv.x, 0, 0, 1.0);
}
