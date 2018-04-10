import argparse

import modelname.task as task


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--style',
                        required=True,
                        type=str,
                        help='Training files local or GCS', nargs='+')
    parser.add_argument('--train-files',
                        required=True,
                        type=str,
                        help='Training files local or GCS', nargs='+')
    parser.add_argument('--eval-files',
                        required=True,
                        type=str,
                        help='Evaluation files local or GCS', nargs='+')
    parser.add_argument('--job-dir',
                        required=True,
                        type=str,
                        help='GCS or local dir to write checkpoints and export model')
    parser.add_argument('--batch-size',
                        type=int,
                        default=40,
                        help='Batch size')
    parser.add_argument('--num-epochs',
                        type=int,
                        default=20,
                        help='Maximum number of epochs on which to train')
    parser.add_argument('--checkpoint-epochs',
                        type=int,
                        default=5,
                        help='Checkpoint per n training epochs')
    parser.add_argument('--content-weight',
                        type=int,
                        default=5,
                        help='')
    parse_args, unknown = parser.parse_known_args()

    task.dispatch(**parse_args.__dict__)
