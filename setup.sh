mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \al_ce@hotmail.fr\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\