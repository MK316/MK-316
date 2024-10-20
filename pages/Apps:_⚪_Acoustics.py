import streamlit as st
from io import BytesIO
import base64

def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Record Vowels", "Tab 4"])

    with tabs[2]:
        st.header("Record Vowels")
        st.write("Click the button to record a vowel sound.")
        components.html("""
            <html>
            <body>
            
            <!-- Include a button to start recording -->
            <button onclick="startRecording(this)">Record</button>
            <button onclick="stopRecording(this)" disabled>Stop</button>
            
            <script>
            var audio_context;
            var recorder;

            function startUserMedia(stream) {
                var input = audio_context.createMediaStreamSource(stream);
                recorder = new Recorder(input);
            }

            function startRecording(button) {
                recorder && recorder.record();
                button.disabled = true;
                button.nextElementSibling.disabled = false;
            }

            function stopRecording(button) {
                recorder && recorder.stop();
                button.disabled = true;
                button.previousElementSibling.disabled = false;

                // Create WAV download link using audio data blob
                createDownloadLink();
                
                recorder.clear();
            }

            function createDownloadLink() {
                recorder && recorder.exportWAV(function(blob) {
                    var url = URL.createObjectURL(blob);
                    var au = document.createElement('audio');
                    var hf = document.createElement('a');
                    
                    au.controls = true;
                    au.src = url;
                    hf.href = url;
                    hf.download = new Date().toISOString() + '.wav';
                    hf.innerHTML = hf.download;
                    document.body.appendChild(au);
                    document.body.appendChild(hf);
                });
            }

            window.onload = function init() {
                try {
                    // webkit shim
                    window.AudioContext = window.AudioContext || window.webkitAudioContext;
                    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
                    window.URL = window.URL || window.webkitURL;
                    
                    audio_context = new AudioContext;
                } catch (e) {
                    alert('No web audio support in this browser!');
                }
                
                navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
                    alert('No live audio input: ' + e);
                });
            };
            </script>

            </body>
            </html>
        """, height=200)
        
if __name__ == "__main__":
    main()
