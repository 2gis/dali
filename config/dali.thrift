service Dali {
    void init (
        1: string remote_url
        2: string capabilities
    )
    void resize (
        1: string resolution
    )
    string take(
        1: string output_path
        2: map<string, string> options
    )
    double compare(
        1: string standard_path
        2: string candidate_path
        3: string result_path
    )
    void stop()
}