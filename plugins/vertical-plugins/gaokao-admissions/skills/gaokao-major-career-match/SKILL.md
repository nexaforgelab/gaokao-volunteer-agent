---
name: gaokao-major-career-match
description: 分析专业适配度和职业匹配。当需要了解专业详情或专业匹配建议时触发。
---

# 专业与职业匹配分析

## 适用场景
- 分析考生与专业的匹配度
- 了解专业就业方向
- 评估专业学习难度
- 检查选科要求匹配

## 不适用场景
- 查询院校录取分数
- 生成志愿方案
- 导入数据

## 输入要求
- 考生选科组合
- 意向专业列表
- 考生偏好（就业/深造/城市）
- 身体条件限制
- 预算限制

## 工作流程
1. 检查选科与专业要求匹配
2. 分析专业就业方向
3. 评估学习难度（数学/物理/编程要求）
4. 检查身体条件限制
5. 评估学费与预算匹配
6. 城市产业匹配分析
7. 输出综合匹配评分

## 输出格式
```json
{
  "major_name": "计算机科学与技术",
  "selection_match": true,
  "employment_direction": ["软件开发", "算法工程师", "数据分析师"],
  "study_difficulty": "high",
  "math_requirement": "high",
  "physics_requirement": "medium",
  "programming_requirement": "high",
  "health_restriction": false,
  "budget_match": true,
  "city_industry_match": 0.8,
  "overall_match_score": 0.85,
  "confidence": 0.7,
  "sources": [],
  "warnings": ["就业情况高度依赖个人能力、学校平台、城市、行业周期"]
}
```

## 风险与边界
- 不得夸大就业前景
- 不得承诺薪资
- 就业率/薪资/升学率必须有来源
- 无来源数据标记 [UNVERIFIED]
- 专业就业情况因人而异，必须提示

## 示例
输入：物理+化学+生物，意向专业=计算机科学与技术
输出：选科匹配，就业方向广泛，学习难度较高，综合匹配分0.85