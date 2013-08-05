struct TOptions {
    1: optional map<string, string> substitute = []
    2: optional list<string> hide_elements = []
    3: optional bool disable_animation = false
}

service TDali {
    void init (
        1: string remote_url
        2: string capabilities
    )
    void resize (
        1: string resolution
    )
    string take(
        1: string save_path
        2: TOptions options
    )
    double compare(
        1: string image1_path
        2: string image2_path
        3: string result_path
    )
    void stop()
}