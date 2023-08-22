#include <opencv2/opencv.hpp>
#include <opencv2/ml.hpp>
#include <iostream>
#include <fstream>

using namespace cv;
using namespace ml;
using namespace std;

int main(){

// Carregar dados de entrada a partir do arquivo
    ifstream inputFile("input_data.txt");
    if (!inputFile.is_open()) {
        cout << "Erro ao abrir o arquivo de entrada." << endl;
        return -1;
    }

    vector<vector<float>> inputVec;
    float inputValue;
    while (inputFile >> inputValue) {
        inputVec.push_back({inputValue});
    }
    inputFile.close();

    // Carregar dados de saída a partir do arquivo
    ifstream outputFile("output_data.txt");
    if (!outputFile.is_open()) {
        cout << "Erro ao abrir o arquivo de saída." << endl;
        return -1;
    }

    vector<vector<float>> outputVec;
    float outputValue;
    while (outputFile >> outputValue) {
        outputVec.push_back({outputValue});
    }
    outputFile.close();

    // Converter vetores para matrizes OpenCV
    //Mat inputTrainingData(inputVec.size(), inputVec[0].size(), CV_32F);
   // Mat outputTrainingData(outputVec.size(), outputVec[0].size(), CV_32F);
   Mat inputTrainingData(inputVec.size()/16, 16, CV_32F);
   Mat outputTrainingData(outputVec.size(), 1, CV_32F);

    for (int i = 0; i < inputVec.size()/16; ++i) {
        for (int j = 0; j < 16; ++j) {
            inputTrainingData.at<float>(i, j) = inputVec[16*i+j][0];
        }
    }

    for (int i = 0; i < outputVec.size(); ++i) {
        for (int j = 0; j < 1; ++j) {
            outputTrainingData.at<float>(i, j) = outputVec[i][j];
        }
    }


    Ptr<ANN_MLP> mlp = ANN_MLP::create();

    Mat layersSize = Mat(3, 1, CV_16U);
    layersSize.row(0) = Scalar(16);
    layersSize.row(1) = Scalar(8);
    layersSize.row(2) = Scalar(1);
    mlp->setLayerSizes(layersSize);

    mlp->setActivationFunction(ANN_MLP::ActivationFunctions::SIGMOID_SYM);
    mlp->setTrainMethod(ANN_MLP::TrainingMethods::BACKPROP);
    TermCriteria term = TermCriteria(TermCriteria::MAX_ITER,141000, 0.00001);
    mlp->setTermCriteria(term);

    Ptr<TrainData> trainingData = TrainData::create(
        inputTrainingData,
        SampleTypes::ROW_SAMPLE,
        outputTrainingData
    );

    //cout << mlp->isTrained() << endl;
    mlp->train(trainingData);
   // cout << mlp->isTrained() << endl;
    Mat prediction;
    mlp->predict(inputTrainingData, prediction);

    cout << prediction << endl;

   // cout << mlp->getWeights(0) << endl << endl<< endl;
   // cout << mlp->getWeights(1) << endl << endl<< endl;
   // cout << mlp->getWeights(2) << endl << endl<< endl;

    mlp->save("treinamento.tre");

}