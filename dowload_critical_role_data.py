from vctube import VCtube


def main():
    yt_dl = VCtube(output_dir='downloaded_dataset', youtube_url='https://www.youtube.com/watch?v=kpkCcb--r90', lang='en')


if __name__ == '__main__':
    main()