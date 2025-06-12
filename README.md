## Google Calendar Tools

**Author:** moritakaho
**Version:** 0.0.1
**Type:** tool

### 説明

このプラグインは Google Calendar とDifyアプリケーションを連携するものです。

このプラグインを利用することで、 Google Calendar に新規イベント登録ができるようになります。

### 事前準備

#### 前提条件

- Google Cloud Platform アカウント
- Google Calendar API が有効化された Google Cloud プロジェクト
- Google Calendar に適切な権限を持つサービスアカウント

#### サービスアカウントの作成

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 新しいプロジェクトを作成するか、既存のプロジェクトを選択
3. プロジェクトで Google Calendar API を有効化：
    1. 「APIとサービス」->「ライブラリ」に移動
    2. 「Google Calendar API」で検索
    3. 「Google Calendar API」をクリック
    4. 「有効にする」をクリック
4. サービスアカウントを作成：
    1. 「IAM と管理」->「サービスアカウント」に移動
    2. 「サービスアカウントを作成」をクリック
    3. サービスアカウント名と説明を入力
    4. 「完了」をクリック
5. サービスアカウント用のキーを作成：
    1. 作成したサービスアカウントをクリック
    2. 「鍵」に移動
    3. 「キーを追加」->「新しい鍵を作成」をクリック
    4. 「JSON」を選択して「作成」をクリック
    5. ダウンロードされたJSONファイルを安全に保存

#### Google Calendar の設定

1. Google Calendar にアクセス
2. 「設定」->「マイカレンダーの設定」-> 連携したいカレンダーを選択
3. 「共有する相手」に次の情報を設定：

    メールアドレス： サービスアカウントのメール

    権限： 予定の変更

#### Difyアプリケーションでの認証

1. Difyアプリケーションで、プラグインセクションに移動
2. 「Google Calendar」をクリック
3. 次の情報で認証：

    credentials_json： サービスアカウントのJSONキーファイルの内容全体

#### Difyアプリケーションでの利用

1. バラメータを設定
    - カレンダーID： 「マイカレンダーの設定」-> 連携したいカレンダー -> カレンダーID
2. 実行






